import torch
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from diffusers import StableDiffusionPipeline
import os
from diffusers import DPMSolverMultistepScheduler
import base64
from io import BytesIO
from flask_cors import CORS






# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Load Stable Diffusion model
print(" Loading Stable Diffusion model... (this may take time)")


# Load Stable Diffusion model
model_path = "./stable_diffusion_models"
pipe = StableDiffusionPipeline.from_pretrained(model_path)

# Ensure correct scheduler settings
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.scheduler.config.use_karras_sigmas = False  # Disable Karras sigmas to avoid index issues

device = "cuda" if torch.cuda.is_available() else "cpu"

# Use float16 only if GPU is available
if device == "cuda":
    pipe.to(device, torch.float16)
    pipe.enable_xformers_memory_efficient_attention()
    pipe.enable_model_cpu_offload()  # Optional for large models
else:
    pipe.to(device, torch.float32)  # Use float32 for CPU

print(" Model loaded successfully!")

# API route to generate an image


@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "fashionable dress")  # Default prompt

    # Generate image
    print(f" Generating image for prompt: {prompt}")

    image = pipe(prompt,num_inference_steps=20, height=512, width=512).images[0]  # Reduce from 768x768 or 1024x1024

    

    # Convert image to base64
    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    image_data = base64.b64encode(image_buffer.getvalue()).decode('utf-8')

    # Return the base64 image
    return jsonify({"image": image_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
