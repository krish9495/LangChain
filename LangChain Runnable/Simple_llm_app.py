from langchain.llms import openai
from langchain.prompts import PromptTemplate

#initialize the llm
llm=openai(model_name="gpt-3.5-turbo",temperature=0.7)

#Create a prompt template

prompt=PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catch blog titled about {topic}."
)

#define the input

topic=input("enter the text")

formatted_prompt=prompt.format(topic=topic)

blog_title=llm.predict(formatted_prompt)

print(blog_title)