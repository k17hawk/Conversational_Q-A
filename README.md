# Conversational Q&A RAG App

This project is a conversational Q&A application that leverages Retrieval-Augmented Generation (RAG) using Hugging Face embeddings and LLaMA3 LLM from Groq API. The app is built using the LangChain framework and implemented with Streamlit, allowing users to upload multiple PDF files and chat with them. The chatbot uses the chain of message history to generate responses.

## Features

## Features

- **Multiple PDF Uploads**: Users can upload multiple PDF files.
- **Conversational Chatbot**: Engage in a conversation with the chatbot which uses the history of messages for context.
- **RAG Integration**: Combines retrieval and generation for accurate and contextually relevant responses.
- **Hugging Face Embeddings**: Utilizes embeddings from Hugging Face for document understanding.
- **LLaMA3 LLM**: Employs LLaMA3 language model from Groq API for generating responses.
- **Chroma Vector Database**: Stores and retrieves embeddings efficiently for fast query responses.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag-qa-chatbot.git
   cd rag-qa-chatbot
   ```
2. **Install the dependencies**
   pip install -r requirements.txt

3. **Obtain API keys for Hugging Face and Groq API.**
Create a .env file in the root directory and add your keys:
env
```
HF=your_huggingface_api_key
GROQ_API_KEY=your_groq_api_key

```
4. **run stramlit**
streamlit run app.py

<img src = "https://github.com/k17hawk/Conversational_Q-A/blob/main/Screenshot%20from%202024-07-24%2019-27-20.png" />
