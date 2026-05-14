from PIL import Image
import streamlit as st
from transformers import BlipForConditionalGeneration, BlipProcessor


@st.cache_resource(show_spinner=False)
def load_blip_models():
    """
    Load and cache BLIP processor + model once.
    Streamlit cache_resource keeps heavy model objects in memory across reruns.
    """
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        return processor, model
    except Exception as error:
        raise RuntimeError(f"Failed to load BLIP model: {error}") from error


def generate_image_description(image: Image.Image) -> str:
    """
    BLIP image captioning:
    1) Convert image to model tensor input.
    2) Run model.generate() for text tokens.
    3) Decode output tokens into readable text.
    """
    processor, model = load_blip_models()
    try:
        inputs = processor(image, return_tensors="pt")
        output_ids = model.generate(**inputs, max_new_tokens=30)
        caption = processor.decode(output_ids[0], skip_special_tokens=True).strip()
        return caption
    except Exception as error:
        raise RuntimeError(f"Failed to generate image description: {error}") from error
