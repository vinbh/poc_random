#!/usr/bin/env bash

# Create folder and navigate into it
mkdir youtube-assistant
cd youtube-assistant

# Set up virtual environment (use python instead of python3 for better cross-platform compatibility)
python -m venv .venv
source .venv/bin/activate

# Install dependencies (some packages might need updates, and langchain-community might not be necessary depending on your use case)
pip install -U python-dotenv langchain openai youtube-transcript-api streamlit faiss-cpu

# Create .env file securely (avoid hardcoding sensitive keys in scripts; add them manually or use environment variables)
echo "OPENAI_API_KEY=\"your-openai-api-key-here\"" > .env

# Test the helper (make sure langchain_helper.py exists and is correctly set up)
python langchain_helper.py  # prints object ID (hoping for no errors, warnings expected)

# Run the chat bot using Streamlit
streamlit run main.py
