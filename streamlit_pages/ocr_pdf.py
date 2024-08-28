import streamlit as st
from app.extract_text_from_file import extract_text_from_docx, extract_text_from_pdf, perform_ocr, load_image
from models.google_gemini import get_response
from prompts import SUMMARY_PROMPT, QUESTION_ANSWER_PROMPT
import os

# Initialize session state variables
if 'text' not in st.session_state:
    st.session_state.text = ''
if 'summary_text' not in st.session_state:
    st.session_state.summary_text = ''
if 'file' not in st.session_state:
    st.session_state.file = None
if 'user_question' not in st.session_state:
    st.session_state.user_question = ''

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def ocr_pdf():
    st.title("OCR and Text Extraction Application")

    storage_directory = st.text_input("Enter the path for storing temporary files:")
    global UPLOAD_DIR
    UPLOAD_DIR = storage_directory
    
    # Check if storage_directory is provided
    if not UPLOAD_DIR:
        st.error("Storage directory path is not provided. Please enter a valid path.")
        return
    
    ensure_directory_exists(UPLOAD_DIR)

    # File uploader
    st.session_state.file = st.file_uploader("Upload Image or Document", type=["png", "jpg", "jpeg", "pdf", "docx"])

    # Language selection for OCR
    languages = st.multiselect(
        'Select languages for OCR',
        ['en', 'ch_sim', 'ja', 'ko', 'fr', 'de', 'es'],  # Add more language codes as needed
        default=['en']
    )

    if st.session_state.file is not None:
        file_extension = st.session_state.file.name.split('.')[-1].lower()

        if file_extension in ["png", "jpg", "jpeg"]:
            image = load_image(st.session_state.file)
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
                    st.session_state.text = extract_text_from_pdf(st.session_state.file)
                st.subheader("Extracted Text from PDF:")


        elif file_extension == "docx":
            doc_button = st.button('Extract text from DOCX')
            if doc_button:
                with st.spinner('Extracting text...'):
                    st.session_state.text = extract_text_from_docx(st.session_state.file)
                st.subheader("Extracted Text from DOCX:")

        st.write(st.session_state.text)

        if st.button("Summarize text"):
            if st.session_state.text != '':
                with st.spinner('Summarizing text...'):
                    st.session_state.summary_text = get_response(SUMMARY_PROMPT + st.session_state.text)
            else:
                st.warning("Please extract text first or check your file")
        st.write(st.session_state.summary_text)

        st.session_state.user_question = st.text_input("Ask your question!")
        if(st.button("Genrate Answer")):
            if st.session_state.user_question != '':
                with st.spinner('Generating answer...'):
                    st.session_state.user_question_answer = get_response(QUESTION_ANSWER_PROMPT + f"Transcription: {st.session_state.text}, Question: {st.session_state.user_question}")
            else:
                st.warning("Please ask a question before generating answer") 
            st.write(st.session_state.user_question_answer)

        