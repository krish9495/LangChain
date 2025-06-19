from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a Detailed Report on the {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='conversational'
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser

result=chain.invoke({'topic':'Unemployemnt in India '})

print(result)
