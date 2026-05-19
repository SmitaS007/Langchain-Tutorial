from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.header('Research Tool')
user_input = st.text_input("Enter your prompt:")

# Create model object
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)
if st.button('Summarize:'):
    result = model.invoke(user_input)
    st.write(result.content)