from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ChatMistralAI(model="mistral-small-2506", temperature=0.7)


messages = []

class ChatRequest(BaseModel):
    message: str
    mode: str


@app.post("/chat")
def chat(request: ChatRequest):
    global messages

    if request.mode == "funny":
        system_prompt = "You are a funny and witty assistant."
    elif request.mode == "professional":
        system_prompt = "You are a professional and formal assistant."
    elif request.mode == "angry":
        system_prompt = "You are an angry assistant."
    else:
        system_prompt = "You are a helpful assistant."

    
    if not messages or messages[0].content != system_prompt:
        messages = [SystemMessage(content=system_prompt)]

    messages.append(HumanMessage(content=request.message))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    return {"response": response.content}
print("Chat History:", messages)