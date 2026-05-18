import streamlit as st
from transformers import pipeline


@st.cache_resource(show_spinner=False)
def load_text_generator():
    """
    Load and cache free Hugging Face text-to-text generation pipeline.
    FLAN-T5 follows instructions better than small causal models for this task.
    Use the small variant to reduce first-run download size and startup time.
    """
    try:
        return pipeline("text2text-generation", model="google/flan-t5-small")
    except Exception as error:
        raise RuntimeError(f"Failed to load text generation model: {error}") from error


def _clean_caption(text: str) -> str:
    cleaned = text.strip().strip("\"'` ").replace("\n", " ")
    if cleaned[:2] in {"1.", "2.", "3."}:
        cleaned = cleaned[2:].strip()
    return " ".join(cleaned.split())


def generate_social_captions(description: str, num_captions: int = 3):
    """
    Generate short social-media-ready captions from an image description.
    """
    text_generator = load_text_generator()

    try:
        captions = []
        for idx in range(num_captions):
            prompt = (
                "Write one short, engaging social media caption.\n"
                "Rules: no hashtags, no quotation marks, under 16 words.\n"
                f"Style variation: {idx + 1} of {num_captions}.\n"
                f"Image description: {description}"
            )

            result = text_generator(
                prompt,
                max_new_tokens=35,
                do_sample=True,
                temperature=0.95,
                top_p=0.92,
                num_return_sequences=1,
            )
            raw = result[0].get("generated_text", "").strip()
            cleaned = _clean_caption(raw)
            if cleaned:
                captions.append(cleaned)

        # Fallback if the model returns fewer lines than requested.
        if len(captions) < num_captions and description:
            while len(captions) < num_captions:
                captions.append(f"Moments like this make the day better.")

        # Ensure exactly requested count and reduce duplicates.
        deduped = []
        seen = set()
        for caption in captions:
            key = caption.lower()
            if key not in seen:
                deduped.append(caption)
                seen.add(key)

        while len(deduped) < num_captions:
            deduped.append(f"Captured in one frame, remembered all day.")

        return deduped[:num_captions]
    except Exception as error:
        raise RuntimeError(f"Failed to generate social captions: {error}") from error
