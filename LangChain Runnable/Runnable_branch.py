from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model=ChatOpenAI()

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough() #default 

)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'Russia V/s Ukraine'}))