# YouTube Assistant Chatbot

This project is a YouTube Assistant chatbot that leverages LangChain, OpenAI's GPT, and Streamlit to interact with YouTube video transcripts. The chatbot can provide detailed insights and summaries from YouTube videos, enabling users to interact with video content in a conversational manner.

## Project Structure

- `langchain_helper.py`: This script contains the core logic for interacting with LangChain and the OpenAI API. It is responsible for processing YouTube transcripts and generating responses based on user input.
  
- `main.py`: This script is the entry point for the Streamlit application. It sets up the user interface and handles interactions between the user and the chatbot.

- `.env`: This file stores environment variables, including your OpenAI API key. Make sure to keep this file secure and avoid sharing it publicly.

## Prerequisites

- Python 3.7 or higher
- `pip` (i'd personally use uv now!!)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/youtube-assistant.git
   cd youtube-assistant

1. ./initial_setup.sh
2. mv *.py youtube-assistant/
3. ./initial_setup.sh
