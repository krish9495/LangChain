from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


spliter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)


loader=PyPDFLoader('dl-curriculum.pdf')
docs=loader.load()

result=spliter.split_documents(docs)
print(result[0])