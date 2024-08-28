import streamlit as st
import os
from app.extract_audio_from_video import extract_audio_from_video
from app.process_video import process_video
from app.transcribe_audio import transcribe_audio
from utils.format_transcription import format_transcription
from models.google_gemini import get_response
from prompts import SUMMARY_PROMPT, QUESTION_ANSWER_PROMPT

# Initialize session state variables
def initialize_state():
    st.session_state.transcription_text = ''
    st.session_state.user_video_question = ''
    st.session_state.user_video_question_answer = ''
    st.session_state.transcription = ''
    st.session_state.summary_video_text = ''
    st.session_state.transcriptions = None
    st.session_state.processed_video_path = None
    st.session_state.audio_path = None

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Initialize session state on first load
if 'transcriptions' not in st.session_state:
    initialize_state()

def video_summary_qa():
    st.title("Transcripto - Video Summarization and Question Answering")

    storage_directory = st.text_input("Enter the path for storing temporary files:")
    global UPLOAD_DIR
    UPLOAD_DIR = storage_directory

    ensure_directory_exists(UPLOAD_DIR)

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        # Reset all session state variables if a new video is uploaded
        initialize_state()

        video_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        # Process the video
        processed_video_path = process_video(video_path)
        st.session_state.processed_video_path = processed_video_path

        # Extract audio from the video
        audio_name = uploaded_file.name + "_audio.wav"
        audio_path = os.path.join(UPLOAD_DIR, audio_name)
        extract_audio_from_video(processed_video_path, audio_path)
        st.session_state.audio_path = audio_path

        # Transcribe the audio
        transcription = transcribe_audio(audio_path)
        transcriptions = format_transcription(transcription)
        st.session_state.transcriptions = transcriptions

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write(uploaded_file.name)
            video_player = st.empty()
            video_player.video(processed_video_path, start_time=0)

        with col2:
            if transcriptions:
                # Display transcriptions with clickable timestamps
                with st.container(border=True, height=300):
                    st.write("Transcription with Timestamps:")
                    for start, transcription in transcriptions:
                        if st.button(f"{start // 60}:{start % 60:02d}", key=f"btn_{start}"):
                            st.session_state.video_start_time = start
                            video_player.video(processed_video_path, start_time=start)
                        st.write(f"{transcription}")

        st.session_state.transcription_text = " ".join([t for _, t in transcriptions])

    # Summarization and QA buttons and logic
    if st.button("Summarize text"):
        if st.session_state.transcription_text:
            with st.spinner('Summarizing text...'):
                st.session_state.summary_video_text = get_response(SUMMARY_PROMPT + st.session_state.transcription_text)
        else:
            st.warning("Please extract text first or check your file")
    st.write(st.session_state.summary_video_text)

    st.session_state.user_video_question = st.text_input("Ask your question!")
    if st.button("Generate Answer"):
        if st.session_state.user_video_question:
            with st.spinner('Generating answer...'):
                st.session_state.user_video_question_answer = get_response(QUESTION_ANSWER_PROMPT + f"Transcription: {st.session_state.transcription_text}, Question: {st.session_state.user_video_question}")
        else:
            st.warning("Please ask a question before generating an answer")
    st.write(st.session_state.user_video_question_answer)