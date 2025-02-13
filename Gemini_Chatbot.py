from PIL import Image
from decouple import config
import google.generativeai as genai
import streamlit as st

API_URL = 'AIzaSyD-r2S_9iG8_UxgCKSHOeaTf1RJ3aye0JU'

genai.configure(
    api_key=API_URL
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "In this chat, respond like you are 9 years old child."

while(True):
    question = input("You: ")

    if(question.strip() == ''):
        break

    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')