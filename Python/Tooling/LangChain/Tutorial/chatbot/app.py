import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ---- event loop fix (required for grpc + streamlit) ----
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


# ---- load env once ----
load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY or ""
os.environ["LANGCHAIN_TRACING_V2"] = "true"


# ---- prompt ----
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)


# ---- lazy, cached LLM creation (THIS is the key fix) ----
@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
    )


# ---- streamlit UI ----
st.title("LangChain Demo with Gemini API")
input_text = st.text_input("Search the topic you want")

if input_text:
    llm = get_llm()
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"question": input_text})
    st.write(result)
