from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are a helfpul assistant'),
    HumanMessage(content="Tell me about Langchain"),
]
result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)