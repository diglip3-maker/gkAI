import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM  # ✅ future-safe official import

# Streamlit UI
st.set_page_config(page_title="Gk Ai")
st.title("gk AI")

# Prompt template
template = """You are a helpful AI assistant.
Question: {question}
Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

# ✅ Modern + No warning
model = OllamaLLM(model="deepseek-r1")  # requires `ollama list` to show deepseek-r1

# Chain
chain = prompt | model

# User input
question = st.chat_input("What's your question?")
if question:
    st.write("**Your Question:**", question)  # 👈 yaha show hoga
    st.write(chain.invoke({"question": question}))
