from secret_key import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open an {cuisine} restaurant, suggest me a name for that" 
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma seperatead list." 
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name' , 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    response = generate_restaurant_name_items("Indian")
    print(response)
