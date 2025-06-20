from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

passthrough=RunnablePassthrough()

prompt1=PromptTemplate(
    template='Generate a Joke about {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()
parser=StrOutputParser()

def word_count(joke_text:str):
    return len(joke_text.split())

joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))