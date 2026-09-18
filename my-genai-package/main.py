from fastapi import FastAPI
from .routers import chat

app = FastAPI(title="Groq Chatbot API", version="1.0.0")

app.include_router(chat.router)

