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

streamlist.multiselect("Pick my fruit",my_fruit_list)
streamlit.dataframe(my_fruit_list)
