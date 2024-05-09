import pandas as pd
import moviepy.editor as mp
import speech_recognition as sr
from gtts import gTTS
import os
from TTS.api import TTS
import tensorflow as tf
import torch 





import streamlit as st
from pydub import AudioSegment

original_audio = AudioSegment.from_file("modi1.wav")

first_2_seconds = original_audio[:2000]
remaining_audio = original_audio[2000:]





def audiototext():


    

    st.title("Audio to Text Conversion")

    # Upload audio file
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])

    if audio_file:
        # Convert audio file to WAV format (required by speech_recognition library)
        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_frame_rate(16000)  # Set sample rate to 16 kHz (required by speech_recognition library)
        audio.export("temp.wav", format="wav")

        # Perform speech-to-text conversion
        r = sr.Recognizer()
        with sr.AudioFile("temp.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)

        st.write("Text Transcription:")
        st.write(text)


            
def text_to_speech(text):
     
    # Initialize TTS model
     tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu='true').to("cuda")

    # Generate audio
     tts.tts_to_file(text, speaker_wav='modi1.wav', file_path="output_synth.wav", language='hi')

    # Return the file path of the synthesized audio
     return "output_synth.wav"

def texttospeech():
    

    # Input text
    text_input = st.text_area("Enter Text")

    if st.button("Convert to Speech"):
        if text_input:
            # Convert text to speech and get the synthesized audio file path
            audio_file_path = text_to_speech(text_input)

            # Display the synthesized audio
            st.audio("output_synth.wav", format="audio/wav")




def generate_video(video_path, audio_path, output_path):
    #Generate video

    

    # Specify the directory path you want to change to
    new_directory = "C:\\Users\\chvai\\Desktop\\streamlit new"

# Change the current working directory
    os.chdir(new_directory)

    
    command = f"python inference.py --face \"C:\\Users\\chvai\\Desktop\\streamlit new\\modi.mp4\" --audio \"C:\\Users\\chvai\\Desktop\\streamlit new\\modi1.wav\" --outfile \"C:\\Users\\chvai\\Desktop\\streamlit new\""

    os.system(command)
    
    if st.button("generate the video"):

       st.video(output_path,format="mp4")


    return output_path
     



            

def main():
    st.header("this is a header")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Audio to Text", "Text to Speech","generate audio"])

    if page == "Home":
        st.title("Welcome to Text-to-Speech and Speech-to-Text App")
    elif page == "Audio to Text":
        audiototext()
    elif page == "Text to Speech":
        texttospeech()
    elif page == "generate audio":    
        video_path = r"C:\\Users\\chvai\\Desktop\\streamlit new\\modi.mp4"
        audio_path = r"C:\Users\chvai\Desktop\streamlit new\modi1.wav"
        output_path = r"C:\Users\chvai\Desktop\streamlit new"
        generate_video(video_path, audio_path, output_path)
        
        


if __name__ == "__main__":
    main()
