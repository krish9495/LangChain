# used openrouter ai becuase hugging face api credit got over
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a Tweet about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a LinkedIN Post about {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'LinkenIN':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'AI'})

print(result)
print(result['tweet'])
print(result['LinkedIN'])
