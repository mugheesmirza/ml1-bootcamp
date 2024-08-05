from langchain_ollama import OllamaLLM
from langchain.core import ChatPromptTemplate

template = """
Answer the following question.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model = "llama3")

response = model.invoke(input="Hello World")

print(response)