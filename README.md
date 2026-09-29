# 📚 Study Tutor Agent

A beginner-friendly AI Study Tutor Agent built with:

- Streamlit
- CrewAI
- Groq
- GPT-OSS 120B
- CrewAI Memory
- Custom CrewAI Tools

## Features

- Explain academic topics
- Beginner, Intermediate and Advanced levels
- Subject selection
- Calculator tool
- Study plan tool
- Agent memory
- Student-friendly explanations
- Practice questions

## Architecture

Streamlit
↓
CrewAI
↓
Study Tutor Agent
↓
Tools + Memory
↓
Groq GPT-OSS 120B

## Environment Variable

The application requires:

GROQ_API_KEY

Never put the API key directly inside the Python code.

## Deployment

The application can be deployed on Render using the GitHub repository.

Build command:

pip install -r requirements.txt

Start command:

streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
