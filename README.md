# 🎙️ VoxFlow Voice AI
### *Next-Generation, Ultra-Low Latency Conversational AI Assistant*

![VoxFlow Banner](https://img.shields.io/badge/VoxFlow-Voice_AI-FF6B00?style=for-the-badge&logo=speaker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Inference-Groq_LPU-F55034?style=for-the-badge&logo=groq&logoColor=white)
![ElevenLabs](https://img.shields.io/badge/TTS-ElevenLabs_v2.5-000000?style=for-the-badge&logo=elevenlabs&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ⚡ Overview

**VoxFlow** is a cutting-edge, real-time voice AI agent engineered for **sub-second latency** and human-like conversational fluidity. Powered by high-speed inference on Groq LPUs and hyper-realistic neural speech synthesis, VoxFlow bridges the gap between instant speech recognition, intelligence processing, and natural voice response.

Whether you're building an interactive voice agent, ambient voice interface, or AI virtual assistant, VoxFlow delivers instantaneous response times with zero lag.

---

## 🚀 Key Features

* **⚡ Sub-Second Latency Pipeline:** Built from the ground up to minimize speech-to-speech delay.
* **🎯 Whisper Large v3 Turbo:** Ultra-fast Automatic Speech Recognition (ASR) via Groq's low-latency hardware.
* **🧠 Llama 3.3 70B Versatile:** Unmatched conversational depth, contextual understanding, and reasoning.
* **🔊 ElevenLabs Turbo v2.5:** High-fidelity, emotional, and low-latency Text-to-Speech (TTS) streaming.
* **🎨 Neon Glassmorphism UI:** Built with Streamlit featuring dynamic states, custom aesthetic HUDs, and real-time audio visualization.

---

## 🛠️ Tech Stack & Engine Architecture

VoxFlow seamlessly stitches together three best-in-class speech and AI technologies:

```
┌─────────────────┐      ┌─────────────────────────┐      ┌──────────────────────┐      ┌─────────────────────────┐
│  🎙️ User Voice  │ ───► │  Whisper Large v3 Turbo │ ───► │  Llama 3.3 70B       │ ───► │  ElevenLabs Turbo v2.5  │
│    (Audio In)   │      │   (ASR via Groq)        │      │  (LLM Engine)        │      │      (TTS Audio Out)    │
└─────────────────┘      └─────────────────────────┘      └──────────────────────┘      └─────────────────────────┘
                                                                                                      │
                                                                                                      ▼
                                                                                           🔊 Dynamic Audio Output
```

| Component | Technology | Description |
| :--- | :--- | :--- |
| **ASR (Speech-to-Text)** | `Whisper Large v3 Turbo` | Ultra-fast transcription powered by Groq |
| **LLM (Brain)** | `Llama 3.3 70B Versatile` | Advanced reasoning and contextual dialogue |
| **TTS (Text-to-Speech)** | `ElevenLabs Turbo v2.5` | Hyper-realistic, streaming voice generation |
| **UI Framework** | `Streamlit + Custom CSS` | Sleek dark-mode futuristic cyber dashboard |

---

## 📦 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Vox-Flow.git
cd Vox-Flow
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### 4. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to start interacting with VoxFlow!

---

## 🎨 UI & System Configuration

VoxFlow includes a customizable sidebar dashboard where you can track live system states:

```markdown
├── ⚙️ VoxFlow Settings
│   ├── 🟢 System Active Indicator
│   ├── 🧩 Engine Details HUD
│   │   ├── ASR: Groq Whisper Large v3 Turbo
│   │   ├── LLM: Llama 3.3 70B Versatile
│   │   └── TTS: ElevenLabs Turbo v2.5
│   └── 🗑️ Clear Chat History / Context Buffer
```

---

## 🛣️ Roadmap

- [ ] **WebRTC Integration:** Full bidirectional audio streaming with zero browser overhead.
- [ ] **Function Calling & Tools:** Allow VoxFlow to browse the live web, execute code, and query databases.
- [ ] **Voice Cloning:** Custom voice profile selector right from the UI sidebar.
- [ ] **Multi-turn Memory Persistence:** Local vector DB memory storage for long-term conversations.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
