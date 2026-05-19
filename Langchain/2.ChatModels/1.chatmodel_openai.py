from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt_4")

result = model.invoke("What is the capital of India?")

print(result)