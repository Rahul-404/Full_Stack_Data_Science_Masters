import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

# here we can give an input in text box
name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0, 100, 25)

st.write(f"Your age is {age}")

if name:
    st.write(f"Hello, {name}")

# select box is like options
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", options=options)
st.write(f"You selected {choice}.")

## create a simple data frame 
df = pd.DataFrame(
    {
        'Name': ["Jhon", "Jane", "Jake", "Jill"],
        'Age': [28, 24, 35, 40],
        'City': ["New York", "Los Angeles", "Chicago", "Houston"]
    }
)

## Display the data frame
st.write("Here is the dataframe:")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)