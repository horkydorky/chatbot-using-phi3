from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse 
from pydantic import BaseModel
import requests
import json
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    history: List[Message]

@app.get("/")
async def read_root():
    return FileResponse('index.html')

async def stream_chat_generator(messages_for_ollama: list):
    try:
        response = requests.post(
            'http://localhost:11434/api/chat',
            json={
                'model': 'phi3',
                'messages': messages_for_ollama,
                'stream': True  
            },
            stream=True
        )
        response.raise_for_status()

        
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                content = chunk.get('message', {}).get('content', '')
                yield content

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        yield "Error: Could not connect to the language model service."
    except Exception as e:
        print(f"An unexpected error occurred during streaming: {e}")
        yield "Error: An internal error occurred."


@app.post('/chat')
async def chat(request: ChatRequest):
    messages_for_ollama = [msg.dict() for msg in request.history]
    
    return StreamingResponse(
        stream_chat_generator(messages_for_ollama), 
        media_type="text/plain"
    )