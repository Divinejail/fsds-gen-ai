import streamlit as st
import pandas as pd
import numpy as np

# 
st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate the basic functionalities of Streamlit.")

#
st.sidebar.header("User Input Features")


user_name = st.sidebar.text_input("What is  your name?","Aditya")


age = st.sidebar.slider("Select your age", 0, 100, 25)

favorite_color = st.sidebar.selectbox("What is your favorite color", ["Blue", "Red", "Green", "Yellow"])

st.header(f"Welcome,{user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}")


st.subheader("Here's some random data:")


# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

# --- Checkbox to show/hide content ---
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# --- Button to trigger an action ---
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")