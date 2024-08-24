import streamlit as st
from streamlit_pages import ocr_pdf, video_summary_qa

st.set_page_config(
    page_title="Transcripto",
    layout="wide",
)

def main():
    st.sidebar.title("🔧 Tools")
    tool = st.sidebar.radio("Select a tool:", ("🏠 Home", "📹 Video Summary Tool", "📄 OCR PDF Summarizer"))
    if tool == "🏠 Home":
        show_home()
    elif tool == "📹 Video Summary Tool":
        video_summary_qa.video_summary_qa()
    elif tool == "📄 OCR PDF Summarizer":
        ocr_pdf.ocr_pdf()
    
    st.sidebar.success("Select a page above")

def show_home():
    st.title("🏠 Welcome to Transcripto")

    st.header("📜 About Transcripto")

    st.write("""
    **Transcripto** is an advanced application designed to revolutionize how you interact with and extract information from your multimedia files. 
    Whether you have videos, PDFs, documents, or images, Transcripto provides a seamless solution for transcription, summarization, and question-answering.
    """)

    st.header("✨ Key Features")
    st.write("""
    Transcripto is packed with powerful features, ensuring you get the most accurate and comprehensive data analysis. Here's what makes Transcripto stand out:
    """)
    st.write("""
    - **📁 Multi-File Support**: Upload videos, PDFs, documents, and images, all in one place. The app handles files up to 200MB, ensuring flexibility and convenience.
    - **🎤 Advanced Speech-to-Text**: Using Wav2Vec2 from Hugging Face, Transcripto transcribes audio from videos with remarkable accuracy, adding timestamps every 30 seconds for easy navigation.
    - **📄 Document Analysis**: PyPDF is employed to extract and analyze textual data from PDFs and documents, allowing for in-depth content summaries and insights.
    - **🖼️ Image Processing**: EasyOCR is used to extract relevant text from images, enabling detailed analysis and the ability to generate summaries and answer questions based on the image content.
    - **💬 Interactive Summaries**: Generate detailed summaries from your files and interact with the content by asking questions to get precise answers.
    """)

    st.header("🛠️ Technology Stack")
    st.write("""
    Transcripto leverages cutting-edge technologies to deliver its powerful features:
    - **🖥️ Streamlit**: Provides a user-friendly interface for easy file uploads and interaction.
    - **🗣️ Wav2Vec2**: A transformer model from Hugging Face for accurate and efficient speech-to-text conversion.
    - **📜 PyPDF**: A robust library for extracting textual data from PDFs and documents.
    - **🔍 EasyOCR**: A reliable tool for extracting text from images, supporting multiple languages and complex layouts.
    """)

    st.header("⚙️ How It Works")
    st.write("""
    Here's a brief overview of the process Transcripto follows to deliver its results:
    1. **📥 File Upload**: Users can upload videos, PDFs, documents, and images through a simple drag-and-drop interface.
    2. **🔊 Audio Extraction**: For video files, the audio is extracted and processed using Wav2Vec2 to generate transcriptions with timestamps.
    3. **📄 Text Extraction**: PDFs and documents are processed using PyPDF, while images are analyzed with EasyOCR to extract text.
    4. **📝 Summarization and QA**: The extracted text is summarized, and users can interact with the content by asking questions to receive precise answers.
    """)

    st.header("🌟 Benefits")
    st.write("""
    Transcripto offers several benefits, making it an essential tool for various use cases:
    - **⏱️ Efficiency**: Save time by quickly extracting and summarizing information from multiple file types.
    - **✔️ Accuracy**: Benefit from state-of-the-art AI models that ensure high accuracy in transcription and text extraction.
    - **🤝 Interactivity**: Engage with your data by asking questions and receiving detailed answers, enhancing understanding and usability.
    - **💼 Convenience**: Handle large files up to 200MB with ease, all within a single application.
    """)

    st.header("🚀 Get Started")
    st.write("""
    Ready to experience the power of Transcripto? Use the sidebar to navigate to the desired tool:
    - Select **📹 Video Summary Tool** to upload a video file, extract its audio, and generate a detailed transcription and summary.
    - Select **📄 OCR PDF Summarizer** to upload a PDF or document, extract text, and get a comprehensive summary and answer questions about the content.
    """)

    st.header("📞 Contact Us")
    st.write("""
    If you have any questions or need support, feel free to reach out. We're here to help you get the most out of Transcripto.
    """)

if __name__ == "__main__":
    main()

