# 1 import streamlit
import streamlit as st

#2 add title yo your app
st.title("My First streamlit App Created by Aditya ")

# 3 add some text
st.write("Welcome! this app calculates the square of a number.")

# 4 create an interactive
st.header("Select a Number")
number = st.slider("Pick a number", 0, 100, 25 )

# calculate and display the  result
st.subheader("Result")
square_number = number * number
st.write(f"The square pf **{number}** is **{square_number}**.")

