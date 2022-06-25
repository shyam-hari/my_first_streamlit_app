import streamlit
import pandas
streamlit.title('My Mom\'s Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')               

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected = streamlit.multiselect("Pick my fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_shown = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_shown)

#New Section for API Interaction
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response,json())
