import streamlit as st
import helper_langchain

st.title("Restaurant Generator")

st.sidebar.title("Cuisine")
cuisine = st.sidebar.selectbox("Select Cuisine", ["Indian", "Chinese", "Italian", "Mexican", "American", "Japanese"])

if cuisine:
    response = helper_langchain.generate_restaurant_name_items(cuisine)
    st.write("***Restaurant Name***")
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("***Menu Items***")
    for item in menu_items:
        st.write("-",item)