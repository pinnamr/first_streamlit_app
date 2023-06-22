import streamlit
streamlit.title('Om Sai Ram')
streamlit.header('Sri Ram')
streamlit.header('Om Sai Ram')
streamlit.text('Om Sai Ram')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avacados'])
streamlit.dataframe(my_fruit_list)
