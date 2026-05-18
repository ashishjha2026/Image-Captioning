# AI Image Caption Generator (Hugging Face Only)

## Description
A Streamlit web app that generates social media captions for any uploaded image using free Hugging Face models. The pipeline consists of two steps: BLIP image captioning produces a textual description of the image, then DistilGPT‑2 generates three concise, hashtag‑free captions.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Workflow Diagram](#workflow-diagram)
- [Dependencies](#dependencies)
- [Usage Example](#usage-example)
- [Offline Operation](#offline-operation)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features
- Fully free, no API keys required.
- Modular code under `utils/`.
- Model caching with `st.cache_resource` to avoid reloads.
- Responsive Streamlit UI with sidebar description.
- Graceful error handling for image loading and model inference.
- Works offline after first run (models cached locally).

## Project Structure
```text
Image-Captioning-HuggingFace/
├── app.py                 # Streamlit entry point, UI and orchestration
├── requirements.txt       # Python dependencies
├── README.md              # Documentation (this file)
└── utils/
    ├── image_caption.py   # BLIP model loader & image description function
    └── social_caption.py  # DistilGPT‑2 loader & caption generation function
```

## Installation
```bash
# Clone the repo (if not already)
git clone https://github.com/yourusername/Image-Captioning-HuggingFace
cd Image-Captioning-HuggingFace

# Install dependencies
pip install -r requirements.txt
```

## Running the App
```bash
streamlit run app.py
```
Open the URL shown in the terminal (usually `http://localhost:8501`).

## Workflow Diagram
```mermaid
graph LR
    A[User uploads image] --> B[BLIP model generates description]
    B --> C[DistilGPT‑2 generates 3 captions]
    C --> D[Display captions in Streamlit UI]
```

## Dependencies
- Python 3.9+
- `streamlit`
- `transformers`
- `torch`
- `Pillow`

All listed in `requirements.txt`.

## Usage Example
1. Drag‑and‑drop a clear image (PNG/JPG/WebP).
2. The app shows a preview and a spinner while generating.
3. After a few seconds you see:
   - **Image Description:** *A dog playing with a ball on a grass field.*
   - **Social Media Captions:**
     1. “Playtime vibes with my furry friend!”
     2. “Nothing beats a sunny fetch session.”
     3. “Chasing joy, one ball at a time.”

## Offline Operation
The first execution downloads model weights from Hugging Face. Subsequent runs reuse the cached files stored in `~/.cache/huggingface/`, allowing completely offline usage on the same machine.

## Troubleshooting
- **Model download fails:** Verify internet connectivity and retry `streamlit run app.py`.
- **Weak caption quality:** Try a different image with a clear subject.
- **Memory errors:** Reduce image size before uploading or run on a machine with more RAM.

## License
This project is licensed under the MIT License. See `LICENSE` for details.


Generate social media captions from an uploaded image using free Hugging Face models with a Streamlit UI.

## Overview
This app uses a two-step inference pipeline:
1. BLIP creates an image description.
2. DistilGPT2 generates 3 social media caption ideas from that description.

No OpenAI API, no API keys, and no paid API calls are used.

## Project Structure
```text
project/
|-- app.py
|-- requirements.txt
|-- README.md
`-- utils/
    |-- image_caption.py
    `-- social_caption.py
```

## Models Used
- Image Captioning: `Salesforce/blip-image-captioning-base`
- Text Generation: `distilgpt2` (Transformers `text-generation` pipeline)

## Features
- Free end-to-end workflow (Hugging Face only)
- Beginner-friendly modular code in `utils/`
- Cached model loading with `@st.cache_resource`
- Responsive Streamlit layout with sidebar + image preview
- Loading spinner and success/error feedback
- Error handling for:
  - Invalid image files
  - Model loading/inference failures
  - Empty generation output

## Workflow
1. Upload an image (`png`, `jpg`, `jpeg`, `webp`)
2. Generate image description with BLIP
3. Generate 3 social captions with DistilGPT2
4. Display outputs as clean caption cards

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

## Requirements
- Python 3.9+
- See [requirements.txt](./requirements.txt)

## Offline Notes
- First run requires internet to download model weights from Hugging Face.
- After models are cached locally, the app can run offline on the same machine.

## Troubleshooting
- If model download fails, check internet and rerun.
- If caption quality is weak for a specific image, try another image with clearer subject focus.
