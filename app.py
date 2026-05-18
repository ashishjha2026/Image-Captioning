import streamlit as st
from PIL import Image
from utils.image_caption import generate_image_description
from utils.social_caption import generate_social_captions

st.set_page_config(page_title="AI Image Caption Generator", page_icon="🖼️", layout="wide")

st.markdown(
    """
    <style>
    .caption-card {
        background: #f7f9fc;
        border: 1px solid #e7ebf3;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("AI Image Caption Generator")
st.caption("100% free workflow using Hugging Face transformer models.")

with st.sidebar:
    st.header("How It Works")
    st.write("1. Upload an image")
    st.write("2. BLIP creates a description")
    st.write("3. FLAN-T5 generates 3 social captions")
    st.info("Models are cached with Streamlit to avoid reloading each rerun.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"],
    help="Supported formats: PNG, JPG, JPEG, WEBP",
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except Exception:
        st.error("Invalid image upload. Please select a valid image file.")
        st.stop()

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("Image Preview")
        st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Generating description and social captions..."):
        try:
            # Step 1: BLIP image captioning to convert image pixels into text.
            description = generate_image_description(image)
            if not description:
                st.error("Image description was empty. Try another image.")
                st.stop()

            # Step 2: FLAN-T5 text generation to create 3 social media caption ideas.
            captions = generate_social_captions(description, num_captions=3)
        except RuntimeError as error:
            st.error(str(error))
            st.stop()
        except Exception as error:
            st.error(f"Unexpected error during inference: {error}")
            st.stop()

    with right_col:
        st.subheader("Generated Output")
        st.success("Caption generation completed successfully.")
        st.markdown(f"**Image Description:** {description}")

        if not captions:
            st.warning("No captions were generated. Try another image.")
        else:
            st.markdown("**Social Media Captions**")
            for idx, caption_text in enumerate(captions, start=1):
                st.markdown(
                    f"<div class='caption-card'><strong>{idx}.</strong> {caption_text}</div>",
                    unsafe_allow_html=True,
                )
