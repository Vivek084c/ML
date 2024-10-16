from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langchain_api_key")

# promt templated
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpfull assistance, please response to the user queries"),
        ("user","Question : {question}")
    ]
)

#srtreamlit framework
st.title("Chatbot")
input_text = st.text_input("Search the topic you want")

#calling openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))