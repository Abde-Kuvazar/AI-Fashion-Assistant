import torch
from diffusers import StableDiffusionPipeline

# Load the model
model_path = "./stable_diffusion_models/model.ckpt"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Generate an image
prompt = "red elegant dress"
image = pipe(prompt).images[0]

# Save the image
image.save("output.png")
print(" Image generated successfully! Check output.png")
