from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server"
)

# ---- Model (MODEL IS REQUIRED) ----
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# ---- Raw chat endpoint ----
add_routes(
    app,
    model,
    path="/chat"
)

# ---- Prompted chain endpoint ----
prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

add_routes(
    app,
    prompt | model,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
