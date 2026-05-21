from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task= "text-generation"
)

model = ChatHuggingFace(llm=llm)   

#1st Prompt -detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
#2nd Prompt - summary of the report
template2 = PromptTemplate(
    template="Write a summary of the following report: {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "The impact of climate change on global agriculture"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
summary = model.invoke(prompt2)

print(summary.content)
