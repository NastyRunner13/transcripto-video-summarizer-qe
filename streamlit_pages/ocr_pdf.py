import streamlit as st
from app.extract_text_from_file import extract_text_from_docx, extract_text_from_pdf, perform_ocr, load_image
from models.google_gemini import get_response

if 'text' not in st.session_state:
    st.session_state.text = ''

def ocr_pdf():
    st.title("OCR and Text Extraction Application")

    # File uploader
    file = st.file_uploader("Upload Image or Document", type=["png", "jpg", "jpeg", "pdf", "docx"])

    # Language selection for OCR
    languages = st.multiselect(
        'Select languages for OCR',
        ['en', 'ch_sim', 'ja', 'ko', 'fr', 'de', 'es'],  # Add more language codes as needed
        default=['en']
    )

    if file is not None:
        file_extension = file.name.split('.')[-1].lower()

        text = ''

        if file_extension in ["png", "jpg", "jpeg"]:
            image = load_image(file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            ocr_button = st.button('Perform OCR')
            if ocr_button:
                with st.spinner('Performing OCR...'):
                    st.session_state.text = perform_ocr(image, languages)
                st.subheader("OCR Result:")


        elif file_extension == "pdf":
            pdf_button = st.button('Extract text from PDF')
            if pdf_button:
                with st.spinner('Extracting text...'):
                    st.session_state.text = extract_text_from_pdf(file)
                st.subheader("Extracted Text from PDF:")


        elif file_extension == "docx":
            doc_button = st.button('Extract text from DOCX')
            if doc_button:
                with st.spinner('Extracting text...'):
                    st.session_state.text = extract_text_from_docx(file)
                st.subheader("Extracted Text from DOCX:")

        st.write(st.session_state.text)

        if st.button("Summarize text"):
            if st.session_state.text != '':
                summary_text = get_response("You are a summarize tool, summarize the following text" + st.session_state.text)
                st.write(summary_text)
            else:
                st.warning("Please extract text first or check your")