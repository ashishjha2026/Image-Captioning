import streamlit as st
from transformers import pipeline


@st.cache_resource(show_spinner=False)
def load_text_generator():
    """
    Load and cache free Hugging Face text generation pipeline.
    DistilGPT2 works with the text-generation task and is fully free to use.
    """
    try:
        return pipeline("text-generation", model="distilgpt2")
    except Exception as error:
        raise RuntimeError(f"Failed to load text generation model: {error}") from error


def _clean_lines(text: str):
    lines = [line.strip(" -\t") for line in text.splitlines()]
    return [line for line in lines if line]


def generate_social_captions(description: str, num_captions: int = 3):
    """
    Prompt the language model with image description text and parse the output
    into 3 short social-media-ready captions.
    """
    text_generator = load_text_generator()

    prompt = (
        "Write 3 short social media captions for this image.\n"
        "Rules: no hashtags, no quotation marks.\n"
        "Format:\n"
        "1. ...\n"
        "2. ...\n"
        "3. ...\n"
        f"Image description: {description}\n"
    )

    try:
        result = text_generator(
            prompt,
            max_new_tokens=90,
            do_sample=True,
            temperature=0.85,
            top_p=0.92,
            num_return_sequences=1,
        )
        generated = result[0]["generated_text"]
        # For causal models, output includes the prompt; keep only new continuation.
        text = generated[len(prompt):].strip() if generated.startswith(prompt) else generated.strip()
        lines = _clean_lines(text)

        captions = []
        for line in lines:
            normalized = line
            if normalized[:2] in {"1.", "2.", "3."}:
                normalized = normalized[2:].strip()
            if normalized:
                captions.append(normalized)
            if len(captions) == num_captions:
                break

        # Fallback if the model returns fewer lines than requested.
        if len(captions) < num_captions and description:
            while len(captions) < num_captions:
                captions.append(f"{description.capitalize()} - caption idea {len(captions) + 1}")

        return captions
    except Exception as error:
        raise RuntimeError(f"Failed to generate social captions: {error}") from error
