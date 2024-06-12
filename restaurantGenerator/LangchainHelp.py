import google.generativeai as palm
from langchain.prompts import PromptTemplate

palm.configure(api_key='AIzaSyBcz_-OT_rwQW_OVdlZ1LCouo5DyHm551Q')

# Define language model instance
llm = palm


def generate_restaurant_name_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open an {cuisine} restaurant, suggest me a name for that."
    )

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated list."
    )

    # Generate restaurant name
    restaurant_name = llm.generate_text(prompt=prompt_template_name.format(cuisine=cuisine))

    # Generate menu items
    menu_items = llm.generate_text(prompt=prompt_template_items.format(restaurant_name=restaurant_name))

    # Print results
    response = {
        'restaurant_name': restaurant_name,
        'menu_items': menu_items
    }
    return response


if __name__ == "__main__":
    print(generate_restaurant_name_items(cuisine))