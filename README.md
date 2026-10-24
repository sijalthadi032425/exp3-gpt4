# Intelligent Email Assistant

An Intelligent Email Assistant built using Python, Streamlit, and Ollama. This application analyzes customer emails to detect intent, retrieves similar historical interactions using Sentence Transformers, generates context-aware replies using LLMs (llama3 via Ollama), improves tone, summarizes the conversation, and saves the interactions.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally.
- Llama3 model pulled in Ollama (`ollama run llama3`).

## Setup Instructions

1. Clone this repository (or copy the files).
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Ollama is running in the background.

## Running the Application

1. Open a terminal in the project directory.
2. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
3. Open your browser to the URL provided (usually `http://localhost:8501`).

## Project Structure

- `main.py`: The main Streamlit application that integrates all modules.
- `input_module.py`: Handles getting and displaying user input.
- `intent_module.py`: Uses Ollama to detect the customer's intent.
- `retrieval_module.py`: Uses Sentence Transformers to find the most similar historical email.
- `reply_module.py`: Uses Ollama to generate a professional reply based on history.
- `tone_module.py`: Modifies the tone of the generated reply using Ollama.
- `summary_module.py`: Generates a short summary of the customer's issue.
- `utils.py`: Helper functions for communicating with the local Ollama instance.
- `data/emails.csv`: Historical email interactions.
- `outputs/generated_reply.txt`: Saved conversation outputs.
