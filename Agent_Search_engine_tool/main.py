import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.agents import AgentExecutor, create_react_agent
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

## Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name="Search")


st.title("Robo 3.0")
"""
Hi, I am search tool Chitti, memory 1 Terabyte. 🤣, I can surf on  Arxiv, wikipedia and DuckDuckGo...
"""

## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assisstant","content":"Hi,I'm a Chitti, Kumar Dahal has created me. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

#input is taken as a prompt
if prompt:=st.chat_input(placeholder="What is the thory of relativity?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    '''
    streaming=True: This parameter enables streaming mode, meaning the responses 
    from the model will be streamed back as they are generated, 
    rather than waiting for the entire response to be completed before receiving it
    
    '''

    llm=ChatGroq(groq_api_key=api_key,model_name="llama-3.1-8b-instant",streaming=True)
    tools=[search,arxiv,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handle_parsing_errors=True)
    

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)
