import requests
import json
import streamlit as st

def call_ollama(prompt, model="llama3.2", system_prompt=None):
    """Call local Ollama API."""
    url = "http://localhost:11434/api/generate"
    
    # We can try llama3, if it fails maybe try phi3 or mistral. 
    # The user is expected to have the model pulled.
    
    full_prompt = prompt
    if system_prompt:
        full_prompt = f"System: {system_prompt}\nUser: {prompt}\nAssistant:"
        
    payload = {
        "model": model,
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to Ollama. Make sure Ollama is running and '{model}' model is installed. Details: {e}")
        return f"Error: Could not connect to Ollama. {e}"
