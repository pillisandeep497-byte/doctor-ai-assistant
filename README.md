# 🩺 Doctor AI Assistant

A conversational medical information assistant built using LangChain, OpenRouter, Pydantic Structured Output, Memory, and Streamlit.

## Features

* Conversational AI Doctor Assistant
* Remembers previous symptoms using chat history
* Structured medical responses
* Disease prediction based on symptoms
* OTC medicine suggestions
* Safety warning signs
* Streamlit chat interface
* OpenRouter LLM integration

## Tech Stack

* Python
* LangChain
* OpenRouter
* Pydantic
* Streamlit

## Architecture

User → Streamlit UI → LangChain Prompt → OpenRouter LLM → Pydantic Output Parser → Structured Response

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/doctor-ai-assistant.git
cd doctor-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

## Example

### User

I have fever and headache.

### Assistant

Question:
How long have you had these symptoms?

Disease:
Need More Information

Precautions:

* Stay hydrated
* Take adequate rest

Danger Signs:

* Difficulty breathing
* Persistent high fever

## Disclaimer

This project provides informational assistance only and is not a substitute for professional medical advice, diagnosis, or treatment.
