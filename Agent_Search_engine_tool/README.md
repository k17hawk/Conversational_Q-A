Tools are interface that an agent, chain or LLM can use to interact with the world.


# Robo 3.0 - AI Search Engine
Robo 3.0 is a powerful search tool designed to assist users with comprehensive searches using multiple sources like Arxiv, Wikipedia, and DuckDuckGo. Built with Streamlit and leveraging open-source large language models (LLM) from Groq, Robo 3.0 provides accurate and contextual search results using generative AI.

# # Features
Arxiv Integration: Fetches and displays scientific papers and articles from Arxiv.
Wikipedia Integration: Retrieves detailed and concise information from Wikipedia.
DuckDuckGo Search: Conducts web searches using DuckDuckGo to provide a broad range of search results.
Interactive Chat: Engages users in a conversational manner, making the search experience more intuitive and user-friendly.
Customizable Settings: Users can input their Groq API key for personalized search experiences.


Enter your Groq API Key:
In the sidebar, input your Groq API Key to activate the search functionalities.

Start a conversation:
Type your query in the chat input. For example, "What is the theory of relativity?"

Code Overview
The core application code is located in app.py. Here's a brief overview of its functionality:

Imports: The necessary libraries and modules are imported.
API Wrappers: Arxiv, Wikipedia, and DuckDuckGo wrappers are initialized for fetching data.
Streamlit UI: The Streamlit interface is set up, including a title, settings sidebar, and chat interface.
Message Handling: The chat history is managed using Streamlit's session state.
Agent Initialization: The search agent is initialized with the specified tools and LLM.
Response Generation: User inputs are processed, and responses are generated and displayed using the search agent.

**Dependencies**

streamlit
langchain_groq
langchain_community
