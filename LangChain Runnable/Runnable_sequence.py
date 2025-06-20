from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='microsoft/Phi-3-mini-4k-instruct',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Write a one liner joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Explain the Following Joke- {text}',
    input_variables=['text']
)


parser=StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result=chain.invoke({'topic':'AI'})
print(result)