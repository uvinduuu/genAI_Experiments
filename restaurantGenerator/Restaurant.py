import streamlit as st
import re
import LangchainHelp

def clean_text(text):
    # Remove specific substrings and unwanted characters
    substrings_to_remove = ['filters=[]', 'safety_feedback=[]', 'result=','Completion(candidates=[...]']
    for substring in substrings_to_remove:
        text = text.replace(substring, '')
    # Remove stars and newlines, then split by comma
    text = re.sub(r'[\*\n\(\)\[\]]', '', text)
    text = text.strip()
    return text

def extract_names(text):
    # Extract restaurant names from text
    return [name.strip() for name in text.split(',') if name.strip()]


st.title('Restaurant Name and Menu Items Generator')

cuisine = st.sidebar.selectbox('Cuisine', ['Chinese', 'Italian', 'Mexican', 'Indian','Arabic','American'])

if cuisine:
    response = LangchainHelp.generate_restaurant_name_items(cuisine)
    restaurant_name = response['restaurant_name']
    menu_items = response['menu_items']

    if not isinstance(restaurant_name, str):
        restaurant_name = str(restaurant_name)
    if not isinstance(menu_items, str):
        menu_items = str(menu_items)

    # Clean the restaurant name and menu items
    cleaned_restaurant_name = clean_text(restaurant_name)
    cleaned_menu_items = clean_text(menu_items)
    
    restaurant_names = extract_names(cleaned_restaurant_name)
    menu_items_list = extract_names(cleaned_menu_items)

     
    if restaurant_names:
        st.write("***Restaurant Name:***")
        st.write(restaurant_names[0])  # Assuming the first name is the main name
    
    if menu_items_list:
        st.write("***Menu Items:***")
        for item in menu_items_list:
            st.write("- " + item)
