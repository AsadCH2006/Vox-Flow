import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from elevenlabs.client import ElevenLabs

# Load Environment Variables
load_dotenv()

# Page Setup
st.set_page_config(page_title="VoxFlow Voice Agent", page_icon="🎙️", layout="centered")
st.title("🎙️ VoxFlow AI Voice Agent")
st.write("Record your message below to interact with your real-time voice assistant.")

# Initialize Clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
eleven_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful voice assistant. Keep answers brief (1-2 sentences)."}
    ]

# Display Previous Conversation
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Audio Recorder Component
from streamlit_mic_recorder import mic_recorder

st.divider()
audio = mic_recorder(
    start_prompt="🔴 Click to Record",
    stop_prompt="⏹️ Stop Recording",
    key="recorder"
)

if audio:
    # 1. Save recorded audio bytes to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio['bytes'])
        temp_audio_path = temp_audio.name

    with st.spinner("Transcribing audio..."):
        # 2. Transcribe via Groq Whisper
        with open(temp_audio_path, "rb") as file:
            transcription = groq_client.audio.transcriptions.create(
                file=(temp_audio_path, file.read()),
                model="whisper-large-v3-turbo",
                response_format="text"
            )
        os.remove(temp_audio_path)

    if transcription.strip():
        # Display User Input
        st.session_state.messages.append({"role": "user", "content": transcription})
        with st.chat_message("user"):
            st.write(transcription)

        # 3. Generate LLM Reply
        with st.spinner("Thinking..."):
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            bot_reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Display Assistant Reply
        with st.chat_message("assistant"):
            st.write(bot_reply)

            # 4. Generate TTS via ElevenLabs & Render Audio Player
            with st.spinner("Synthesizing voice..."):
                audio_bytes = eleven_client.text_to_speech.convert(
                    text=bot_reply,
                    voice_id="JBFqnCBsd6RMkjVDRZzb",  # Your custom or preferred voice ID
                    model_id="eleven_turbo_v2_5"
                )
                
                # Collect audio bytes into a single buffer for Streamlit audio element
                audio_data = b"".join(chunk for chunk in audio_bytes)
                st.audio(audio_data, format="audio/mp3", autoplay=True)