# Transcripto: Video Summarization with QE

Transcripto is an advanced application designed to revolutionize how you interact with and extract information from your multimedia files. Whether you have videos, PDFs, documents, or images, Transcripto provides a seamless solution for transcription, summarization, and question-answering.

## Features

- 📁 **Multi-File Support**: Upload videos, PDFs, documents, and images, all in one place. The app handles files up to 200MB.
- 🎤 **Advanced Speech-to-Text**: Transcribe audio from videos with Wav2Vec2 from Hugging Face, adding timestamps every 30 seconds.
- 📄 **Document Analysis**: Extract and analyze text from PDFs and documents using PyPDF.
- 🖼️ **Image Processing**: Use EasyOCR to extract text from images.
- 💬 **Interactive Summaries**: Generate summaries and ask questions based on the content.

## Technology Stack

- **🖥️ Streamlit**: Provides a user-friendly interface for easy file uploads and interaction.
- **🗣️ Wav2Vec2**: A transformer model from Hugging Face for accurate and efficient speech-to-text conversion.
- **📜 PyPDF**: A robust library for extracting textual data from PDFs and documents.
- **🔍 EasyOCR**: A reliable tool for extracting text from images, supporting multiple languages and complex layouts.

## Prerequisites
Before running Transcripto, ensure you have the following installed on your local system:
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Installation
### Step 1: Clone the Repository
If you have Git installed, you can clone the repository using the following command:
```bash
git clone https://github.com/NastyRunner13/transcripto-video-summarizer-qe.git
cd transcripto-video-summarizer-qe
```
Alternatively, download the ZIP file from the repository and extract it.

### Step 2: Set Up a Virtual Environment
Create a virtual environment to isolate the dependencies for this project.
```bash
python3 -m venv transcripto-env
source transcripto-env/bin/activate  # On Windows, use `transcripto-env\Scripts\activate`
```

### Step 3: Install Required Python Packages
Navigate to the project directory and install the required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a .env file in the root directory and add any required environment variables. Example:
```bash
GEMINI_API_KEY = your_gemini_api_key
```

### Step 5: Prepare the Storage Directory
Ensure that the directory for storing temporary files exists:
```bash
mkdir -p /path/to/your/storage/directory
```

## Running the Application
### Step 1: Launch the Streamlit App
Run the Streamlit app using the following command:
```bash
streamlit run main.py
```

### Step 2: Use the Application
- **Home Page**: Provides an overview of Transcripto and its features.
- **Video Summary Tool**: Upload a video, transcribe audio, summarize text, and ask questions.
- **OCR PDF Summarizer**: Upload an image, PDF, or DOCX file to extract and summarize text, and ask questions.

## Directory Structure
```css
transcripto-video-summarizer-qe/
│
├── app/
│   ├── extract_audio_from_video.py
│   ├── process_video.py
│   ├── transcribe_audio.py
│   └── extract_text_from_file.py
│
├── models/
│   └── google_gemini.py
│   └── wav2vac2.py
│
├── streamlit_pages/
│   └── ocr_pdf.py
│   └── video_summary_qa.py
│
├── utils/
│   └── format_transcription.py
|   └── is_16_9_ratio.py
│
├── prompts.py
├── main.py
├── requirements.txt
└── README.md
```

## Usage Instructions
### Video Summary Tool
1. Navigate to the Video Summary Tool from the sidebar.
2. Enter the path for storing temporary files.
3. Upload a video file (MP4, AVI, MOV, MKV).
4. The application will process the video, extract audio, transcribe it, and display the transcription with clickable timestamps.
5. Summarize the transcription or ask a question to receive an answer.

### OCR PDF Summarizer
1. Navigate to the OCR PDF Summarizer from the sidebar.
2. Enter the path for storing temporary files.
3. Upload an image (PNG, JPG), PDF, or DOCX file.
4. Perform OCR on images or extract text from PDFs/DOCX files.
5. Summarize the extracted text or ask a question to receive an answer.

### Troubleshooting
- Ensure the correct path is provided for storing temporary files.
- Verify that all dependencies are correctly installed by checking requirements.txt.
- Check if the API key is correctly set in the .env file for accessing external models.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For support, contact [Prince Gupta] at [princegupta1586@gmail.com] or [Dishita Aggarwal] at [dishitaaggarwal30@gmail.com].
