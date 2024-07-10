import streamlit as st
import easyocr
from PIL import Image
import numpy as np
from PyPDF2 import PdfReader
import docx

def load_image(image_file):
    img = Image.open(image_file)
    return img

def perform_ocr(img, languages):
    # Convert PIL Image to numpy array
    img_array = np.array(img)
    
    reader = easyocr.Reader(languages)
    result = reader.readtext(img_array)
    
    # Combine all the detected text into a single string
    text = ' '.join([detection[1] for detection in result])
    
    return text

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text