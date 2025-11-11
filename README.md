Generative AI for Fashion Design

**Text2Fashion** is a lightweight yet research-driven GenAI project that transforms *natural language outfit descriptions* into realistic **fashion images**.  
The system integrates **Stable Diffusion XL**, **ControlNet**, and **IP-Adapter** pipelines locally to ensure controllable, high-quality image synthesis — all running on CPU/GPU with minimal dependencies.

---

## ✨ Overview

> “Describe it, See it.”

Text2Fashion bridges creativity and machine intelligence.  
Users can describe an outfit — e.g., *“black velvet blazer with gold embroidery, runway lighting, formal look”* — and the system generates a corresponding realistic fashion image.  

The project aims to make **AI-assisted fashion prototyping** accessible and fast for designers, brands, and researchers.

---

## 🧠 Core Technologies

| Component | Description |
|------------|-------------|
| **Stable Diffusion XL (SDXL)** | High-resolution text-to-image generation pipeline. |
| **ControlNet** | Structural guidance for pose, edges, and garment layout. |
| **IP-Adapter** | Image prompt adapter for better style and composition consistency. |
| **Flask** | Lightweight backend framework for serving local models and web UI. |
| **Gradio-inspired UI** | Clean, responsive interface for interactive text-to-image generation. |
| **Pillow / OpenCV** | Image decoding, post-processing, and visualization. |

---

## ⚙️ Architecture

User Prompt
↓
Text Encoder (CLIP / OpenCLIP)
↓
Stable Diffusion XL Pipeline
↙︎ ↘︎
ControlNet IP-Adapter
↓ ↓
Feature Fusion & Denoising
↓
Generated Fashion Image


---

## 💡 Features

- 🪄 **Text-to-Fashion Image Generation** — generate realistic outfit visuals from simple text prompts.  
- 🧍 **ControlNet Guidance** — preserve body structure or pose when desired.  
- 🎨 **IP-Adapter Consistency** — achieve stylistic coherence across multiple images.  
- 🧵 **Automatic Palette Extraction** — show dominant colors and tones in the generated look.  
- 🪞 **Style & Accessory Suggestions** — basic NLP-based suggestions for accessories or complementary garments.  
- 🖼️ **Variation Gallery** — view and switch between multiple generated looks.  
- 💾 **Download & Lookbook Mode** — save generated outfits as images for portfolio building.  
- 🌈 **Modern UI** — Aesthetic, trendy, glassmorphic interface built with responsive CSS.

---

🧬 Model Components (Local)

Stable Diffusion XL (weights loaded via diffusers)

ControlNet for edge/pose conditioning (optional)

IP-Adapter for maintaining consistent fashion style

Autoencoder KL from SDXL for efficient image decoding

All models are locally cached from the Hugging Face model hub or pre-downloaded and stored under

<img width="1844" height="912" alt="Screenshot 2025-11-11 163243" src="https://github.com/user-attachments/assets/48dad07d-1481-461b-a6d2-f1d192929b8c" />

<img width="1869" height="905" alt="Screenshot 2025-11-11 163306" src="https://github.com/user-attachments/assets/b816fdf7-e331-41e4-b294-43701c23c51f" />



