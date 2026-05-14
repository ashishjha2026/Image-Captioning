# AI Image Caption Generator (Hugging Face Only)

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
