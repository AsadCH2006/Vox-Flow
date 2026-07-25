import os
import time
from dotenv import load_dotenv
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from groq import Groq
from elevenlabs.client import ElevenLabs
from elevenlabs import play

# Load environment variables from .env file
load_dotenv()

# Initialize API clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
eleven_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Configure your Voice ID (defaults to 'George' if not set in .env)
# Find custom voice IDs in ElevenLabs dashboard -> Voices -> Click Voice -> ID
VOICE_ID = os.getenv("ELEVEN_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")

def record_audio(filename="input.wav", duration=4, samplerate=16000):
    """Records audio from the microphone for a fixed duration."""
    print("\n🎙️ Listening (speak now)...")
    audio_data = sd.rec(
        int(duration * samplerate), 
        samplerate=samplerate, 
        channels=1, 
        dtype='int16'
    )
    sd.wait()
    wav.write(filename, samplerate, audio_data)
    return filename

def transcribe(file_path):
    """Transcribes audio file to text using Groq Whisper."""
    with open(file_path, "rb") as file:
        transcription = groq_client.audio.transcriptions.create(
            file=(file_path, file.read()),
            model="whisper-large-v3-turbo",
            response_format="text"
        )
    return transcription.strip()

def generate_reply(user_text):
    """Generates LLM response using Groq (Llama 3.3)."""
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system", 
                "content": "You are a concise voice assistant. Limit responses to 1-2 clear sentences."
            },
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content

def speak(text):
    """Converts text to speech using ElevenLabs and plays audio."""
    print(f"🤖 Agent: {text}")
    
    # Updated ElevenLabs v1.x+ stream conversion method
    audio_stream = eleven_client.text_to_speech.convert_as_stream(
        text=text,
        voice_id=VOICE_ID,
        model_id="eleven_turbo_v2_5"
    )
    
    # Play stream back through output speakers
    play(audio_stream)

def main():
    print("=== VoxFlow Voice Agent Online ===")
    print("Press Ctrl+C in terminal to exit.\n")
    
    try:
        while True:
            # 1. Capture user voice
            audio_file = record_audio(duration=4)
            
            # 2. Convert speech to text
            user_text = transcribe(audio_file)
            
            if not user_text:
                continue
                
            print(f"👤 You: {user_text}")
            
            # Check for exit command
            if any(word in user_text.lower() for word in ["exit", "quit", "stop"]):
                speak("Goodbye!")
                break

            # 3. Get LLM response
            reply = generate_reply(user_text)
            
            # 4. Synthesize voice & play
            speak(reply)
            
    except KeyboardInterrupt:
        print("\nShutting down VoxFlow...")

if __name__ == "__main__":
    main()