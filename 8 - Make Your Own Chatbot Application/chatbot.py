from dotenv import load_dotenv,find_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import (SystemMessagePromptTemplate,
                                    HumanMessagePromptTemplate,
                                    ChatPromptTemplate,
                                    MessagesPlaceholder)
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

import streamlit as st

load_dotenv(find_dotenv())

st.title("Make Your Own Chatbot")
st.write("A General purpose ChatBot")

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///chat_history.db")

user_id = st.text_input(label='Enter your user id',value='user_101')

if st.button(label="Start New Conversation !!!"):
    st.session_state.chat_history = []
    history = get_session_history(user_id)
    history.clear()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

## LLM
base_url = "http://localhost:11434"
model = "llama3.2:3b"

llm = ChatOllama(
    base_url=base_url,
    model=model
)

system = SystemMessagePromptTemplate.from_template("You are helpful assistant.")
human = HumanMessagePromptTemplate.from_template("{input}")

messages = [system, MessagesPlaceholder(variable_name='history'), human]

prompt = ChatPromptTemplate(messages=messages)

chain = prompt | llm | StrOutputParser()


runnable_with_history = RunnableWithMessageHistory(chain, get_session_history, 
                                                   input_messages_key='input', 
                                                   history_messages_key='history')

def chat_with_llm(user_id, input):
    for chunk in runnable_with_history.stream({'input': input}, config={'configurable': {'session_id': user_id}}):
        yield chunk


prompt = st.chat_input("What is up ?")

if prompt:
    st.session_state.chat_history.append({
        'role': 'user',
        'content': prompt
    })

    with st.chat_message('user'):
        st.markdown(prompt)
    
    with st.chat_message('assistant'):
        response = st.write_stream(chat_with_llm(user_id=user_id,input=prompt))
    
    st.session_state.chat_history.append({
        'role': 'assistant',
        'content': response
    })
