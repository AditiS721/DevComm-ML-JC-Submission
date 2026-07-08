import gradio as gr
import ollama
import base64
from pathlib import Path
import tempfile
import os

class MultimodalChatbot:
    def __init__(self, text_model="llama3.2:1b", vision_model="llava:7b"):
        self.text_model = text_model
        self.vision_model = vision_model
        self.conversation_history = []
    
    def encode_image(self, image_path):
        """Encode image to base64 for Ollama"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def process_file(self, file_path):
        """Process uploaded files and extract text"""
        try:
            file_ext = Path(file_path).suffix.lower()
            
            if file_ext in ['.txt', '.md', '.py', '.csv']:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()[:2000]  # Limit text length
            else:
                return f"File type {file_ext} uploaded. Path: {file_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def chat(self, message, history, image=None, file=None):
        """
        Handle text, image, and file inputs
        """
        try:
            # Process file if uploaded
            file_content = ""
            if file is not None:
                file_content = self.process_file(file.name)
                message = f"{message}\n\nUploaded file content:\n{file_content}"
            
            # Handle image input
            if image is not None:
                # Use vision model for image understanding
                image_data = self.encode_image(image)
                
                # Create message with image
                messages = [{
                    'role': 'user',
                    'content': message if message else "Describe this image",
                    'images': [image_data]
                }]
                
                response = ollama.chat(
                    model=self.vision_model,
                    messages=messages
                )
            else:
                # Text-only conversation
                messages = []
                for human, assistant in history:
                    messages.append({"role": "user", "content": human})
                    messages.append({"role": "assistant", "content": assistant})
                messages.append({"role": "user", "content": message})
                
                response = ollama.chat(
                    model=self.text_model,
                    messages=messages
                )
            
            return response['message']['content']
        
        except ollama.ResponseError as e:
            return f"Model error: {str(e)}. Make sure you've pulled the required models."
        except Exception as e:
            return f"Error: {str(e)}. Check if Ollama server is running."

# Create the chatbot instance
chatbot = MultimodalChatbot()

# Custom CSS for better UI
custom_css = """
.gradio-container {
    max-width: 1000px !important;
    margin: auto !important;
}
.chat-message {
    padding: 15px !important;
    border-radius: 8px !important;
}
"""

# Build the Gradio interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Advanced Multimodal AI Chatbot")
    gr.Markdown("*Powered by Ollama - 100% Local & Private*")
    
    with gr.Tab("💬 Chat"):
        chatbot_interface = gr.ChatInterface(
            fn=chatbot.chat,
            additional_inputs=[
                gr.Image(type="filepath", label="Upload Image (optional)"),
                gr.File(label="Upload File (optional)")
            ],
            title="",
            description="",
            examples=[
                ["Hello! Who are you?"],
                ["Explain quantum computing in simple terms"],
                ["Write a Python function to calculate fibonacci sequence"]
            ]
        )
    
    with gr.Tab("📊 System Info"):
        gr.Markdown("### Model Information")
        models_info = gr.Textbox(
            label="Installed Models",
            value="Run 'ollama list' in terminal to see installed models",
            interactive=False
        )
        
        gr.Markdown("### Tips")
        gr.Markdown("""
        - **Text Model**: llama3.2:1b (fast, lightweight)
        - **Vision Model**: llava:7b (image understanding)
        - **Privacy**: All processing happens locally
        - **Speed**: Depends on your hardware
        """)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )