import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # loads GOOGLE_API_KEY from .env

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # good for free tier + chat
        temperature=0.3,
    )
