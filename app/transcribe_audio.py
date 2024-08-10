import torch
import torchaudio
from pydub import AudioSegment
import os
from models.wav2vac2 import wav2vec2model
import streamlit as st

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def transcribe_audio(audio_path, segment_length=30):

    model ,processor = wav2vec2model()

    try:
        audio = AudioSegment.from_wav(audio_path)
        duration = int(len(audio) / 1000)  # Convert to seconds and ensure it's an integer

        transcriptions = []
        for start in range(0, duration, segment_length):
            end = min(start + segment_length, duration)
            segment = audio[start * 1000:end * 1000]
            segment_path = os.path.join("C:/Users/princ/Desktop/tempFiles", f"segment_{start}_{end}.wav")
            segment.export(segment_path, format="wav")

            waveform, sample_rate = torchaudio.load(segment_path)

            # Resample to 16kHz if needed
            resample_rate = 16000
            if sample_rate != resample_rate:
                resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=resample_rate)
                waveform = resampler(waveform)

            inputs = processor(waveform.squeeze().numpy(), return_tensors="pt", padding="longest").to(device)

            with torch.no_grad():
                logits = model(inputs.input_values).logits

            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = processor.batch_decode(predicted_ids)[0]
            transcriptions.append((start, transcription))

            os.remove(segment_path)

        return transcriptions
    except Exception as e:
        st.error(f"An error occurred during transcription: {e}")