from fastapi import FastAPI
from chatbot import chat

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ritchat API working"}

@app.get("/chat")
def chat_api(msg: str):
    return {"response": chat(msg)}
