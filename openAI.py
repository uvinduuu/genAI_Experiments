from secret_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6) #how creative the llm is
name = llm("I want to open an Indian restaurent, suggest me a name for that.")
print(name)

from langchain.prompts import PromptTemplate

prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template - "I want to open an {cuisine} restaurent, suggest me a name for that' 
)

prompt_template_name.format(cuisine="Italian")

from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt_template_name)
chain.run("Mexican")
