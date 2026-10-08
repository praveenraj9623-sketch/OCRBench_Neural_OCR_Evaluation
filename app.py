import streamlit as st

st.set_page_config(
    page_title="OCRBench",
    page_icon="🔍",
    layout="wide",
)

st.title("OCRBench")
st.subheader("Neural OCR Evaluation")
st.info("Prototype in progress. OCR inference is being implemented.")

uploaded = st.file_uploader(
    "Upload a document image",
    type=["png", "jpg", "jpeg"],
)

if uploaded is not None:
    st.write({
        "Filename": uploaded.name,
        "Size (KB)": round(uploaded.size / 1024, 2),
    })

    try:
        st.image(uploaded, caption="Uploaded document image")
        st.caption("No OCR recognition or accuracy evaluation has run yet.")
    except Exception:
        st.error("Unable to preview this file. Upload a valid PNG or JPEG.")
else:
    st.caption("Upload an image to begin.")
