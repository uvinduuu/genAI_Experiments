from secret_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6) #how creative the llm is
'''
name = llm("I want to open an Indian restaurant, suggest me a name for that.")
print(name)
'''

from langchain.prompts import PromptTemplate

prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template = "I want to open an {cuisine} restaurant, suggest me a name for that" 
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

#prompt_template_name.format(cuisine="Italian")

from langchain.chains import LLMChain

#name_chain.run("Mexican")

prompt_template_items = PromptTemplate(
  input_variables = ['restaurant_name'],
  template = "Suggest some menu items for {restaurant_name}. Return it as a comma seperatead list." 
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

'''
#for one output
from langchain.chains import SimpleSequentialChain

chain = SimpleSequentialChain(chains = [name_chain, food_items_chain])
print(response)
'''

#multiple outputs
from langchain.chains import SequentialChain

chain = SequentialChain(
  chains = [name_chain, food_items_chain],
  input_variables = ['cuisine'],
  output_variables = ['restaurant_name' , 'menu_items']
)

chain({'cuisine' : 'Arabic'})from secret_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6) #how creative the llm is
name = llm("I want to open an Indian restaurant, suggest me a name for that.")
print(name)

from langchain.prompts import PromptTemplate

prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template - "I want to open an {cuisine} restaurant, suggest me a name for that" 
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

'''
prompt_template_name.format(cuisine="Italian")
from langchain.chains import LLMChain
name_chain.run("Mexican")
'''

prompt_template_items = PromptTemplate(
  input_variables = ['restaurant_name'],
  template - "Suggest some menu items for {restaurant_name}. Return it as a comma seperatead list." 
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

#for one output
from langchain.chains import SimpleSequentialChain

chain = SimpleSequentialChain(chains = [name_chain, food_items_chain])
print(response)

#multiple outputs
from langchain.chains import SequentialChain

chain = SequentialChain(
  chains = [name_chain, food_item_chain],
  input_variables = ['cuisine'],
  output_variables = ['restaurant_name' , 'menu_items']
)

chain({'cuisine' : 'Arabic})
