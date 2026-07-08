import gradio as gr
import ollama

def chat_with_model(message, history):
    try:
        messages = []
        for human, assistant in history:
            messages.append({"role": "user", "content": human})
            messages.append({"role": "assistant", "content": assistant})
        messages.append({"role": "user", "content": message})
        
        response = ollama.chat(
            model='llama3.2:1b',
            messages=messages
        )
        
        return response['message']['content']
    
    except Exception as e:
        return f"Error: {str(e)}. Is Ollama running?"

# Create Gradio interface without theme parameter
demo = gr.ChatInterface(
    fn=chat_with_model,
    title="My Local AI Chatbot",
    description="Private chatbot powered by Ollama"
)

if __name__ == "__main__":
    demo.launch(share=False)