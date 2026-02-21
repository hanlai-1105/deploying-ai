from email.mime import message
import gradio as gr

# Import services
from services.API_service import get_weather
from services.semantic_service import semantic_search
from services.tool_service import create_study_plan

# Conversation memory
chat_history = []

def assistant_reply(message, history):
    text = message.lower()

    blocked_topics = ["cats", "dogs", "horoscope", "zodiac", "taylor swift"]
    if any(word in text for word in blocked_topics):
        response = "Sorry, I can’t discuss that topic."

    # Service 1: API
    elif "weather" in text:
        response = get_weather("Toronto")

    # Service 2: Semantic Search
    elif "what is" in text or "explain" in text or "define" in text:
        response = semantic_search(message)
    
    #Service 3: Study Plan Generation Tool
    elif "study plan" in text:
        response = create_study_plan(message)

    else:
        response = "I can help with weather or knowledge questions!"

    history.append((message, response))
    return history, history


with gr.Blocks() as demo:
    gr.Markdown("### AI Study Assistant ☁️")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask something...")

    msg.submit(assistant_reply, [msg, chatbot], [chatbot, chatbot])

demo.launch()
