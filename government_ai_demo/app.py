import streamlit as st
import fitz

st.set_page_config(
    page_title="AI Document Verification",
    layout="wide"
)

st.title("📄 AI Document Verification System")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully")

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    extracted_text = ""

    for page in pdf:
        extracted_text += page.get_text()

    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        extracted_text,
        height=300
    )

document_type = "Unknown"

if "aadhaar" in text.lower():
    document_type = "Aadhaar Card"

elif "income tax department" in text.lower():
    document_type = "PAN Card"

elif "passport" in text.lower():
    document_type = "Passport"

st.subheader("Detected Document Type")

st.success(document_type)
# Health Score Calculation

score = 0

if len(text) > 100:
    score += 30

if document_type != "Unknown":
    score += 40

if "address" in text.lower():
    score += 15

if "dob" in text.lower():
    score += 15
