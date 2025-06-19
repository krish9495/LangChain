from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='chat-completion'
)

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description="Name of the Person")
    age:int =Field(gt=18,description='Age of the Person')
    city:str = Field(description='Name of the City the person belongs to ')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name , age, city of the fictional{place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt=template.invoke({'place':'indian'})
result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)