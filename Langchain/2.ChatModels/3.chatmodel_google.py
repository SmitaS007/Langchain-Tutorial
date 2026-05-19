from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenAI(model = "gemini-2.0-pro")
result = model.invoke("What is the capital of India?")
print(result.content)
