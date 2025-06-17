from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

document=[
    "Delhi is the capital of india",
    "Krish is a good guy",
    "I'm learning very passionately"
]

result=embedding.embed_documents(document)

print(str(result))