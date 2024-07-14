from moviepy.editor import VideoFileClip
import streamlit as st

def extract_audio_from_video(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        st.success(f"Audio extracted and saved to {audio_path}")
    except Exception as e:
        st.error(f"An error occurred while processing the video: {e}")