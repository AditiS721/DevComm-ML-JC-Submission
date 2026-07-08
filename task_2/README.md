
# Ollama Chatbot

A private AI chatbot powered by Ollama, running locally on your machine.

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.com/download) installed on your system
- At least 6GB of free disk space (for models)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ollama-chatbot.git
cd ollama-chatbot
```

### 2. Set Up Virtual Environment

**Windows:**
```cmd
python -m venv chatbot_env
chatbot_env\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
```

### 3. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 4. Pull AI Models

```cmd
# Required: Text chat model (~1.5GB)
ollama pull llama3.2:1b

# Optional: Image understanding model (~4GB)
ollama pull llava:7b
```

### 5. Start Ollama Service

Open a new terminal and run:

```cmd
ollama serve
```

Keep this terminal running in the background.

### 6. Launch the Chatbot

In your first terminal (with virtual environment activated):

```cmd
python basic_chatbot.py
```

### 7. Access the Chatbot

- Open any web browser (Chrome, Firefox, Edge, Safari)
- Go to: **http://127.0.0.1:7860**
- The chat interface will appear with a text box
- Type your message and press Enter to start chatting
- The AI will respond within a few seconds

Your private AI assistant is now ready to use.

## Features

- 🏠 **Fully Local** - All processing happens on your machine
- 🔒 **Private** - No data sent to external servers
- 💬 **Text Chat** - Conversational AI with context awareness
- 🖼️ **Image Understanding** - Describe and analyze images 
- 🎨 **Clean Interface** - User-friendly Gradio web UI

## Troubleshooting

- **Ollama not found**: Make sure Ollama is installed and added to your PATH
- **Port in use**: Change the port in `basic_chatbot.py` if 7860 is occupied
- **Slow responses**: First message may be slower as the model loads
- **Model errors**: Ensure you've pulled the required models with `ollama pull`

## Requirements

```
gradio
ollama
Pillow
```

