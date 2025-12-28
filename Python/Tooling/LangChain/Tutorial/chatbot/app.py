from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import os

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful assistant, please respond to the user queries"),
    ("user", "Question: {question}")
  ]
)

# streamlit framework
st.title("Langchain Demo with Gemini API")
input_text = st.text_input("Search the topic you want")

# Gemini LLM
