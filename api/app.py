from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    mode: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def chat(data: ChatRequest):
    return {"response": f"You said: {data.message} in {data.mode} mode"}
