from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text_generation'
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template="Generate 5 interesting fact about {topic}",
    input_variables=['topic']
)



parser=StrOutputParser()

chain= prompt|model|parser
result=chain.invoke({'topic':'Hunar Tribe'})
# print(result)

chain.get_graph().print_ascii()