# FastAPI Chat with Ollama (phi3)

This project is a simple **chat backend** built with [FastAPI](https://fastapi.tiangolo.com/).  
It connects to [Ollama](https://ollama.ai/) to stream chat responses from a local LLM (default: `phi3`).  

---

## Features

- FastAPI backend with CORS enabled (ready for any frontend)  
- `/` serves an `index.html` file (basic chat UI)  
- `/chat` endpoint proxies chat messages to **Ollama**  
- Streams responses back in real time  

---

## Requirements

- Python 3.9+  
- installed and running locally  
- `phi3` (or another Ollama model like `mistral`, `tinyllama`, etc.
- I tried mistral,tinyllama but it worked comparatively better using phi3)  

---

## Installation

1. Clone this repo (or copy the files).  
2. Install dependencies:  

   ```bash
   pip install fastapi uvicorn requests pydantic
   Make sure Ollama is installed and a model is available.
To check your models:

ollama list


To pull phi3 if you don’t already have it:

ollama pull phi3

Running the App

Start the FastAPI server:

uvicorn main:app --reload


By default, it runs at:
👉 http://127.0.0.1:8000/

API Endpoints
GET /

Serves the index.html file (chat UI).

POST /chat

Streams responses from the Ollama model.

Request body:

{
  "history": [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi, how can I help you?"}
  ]
}


Response:
Plain text stream of the assistant’s reply.


