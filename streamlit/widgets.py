import streamlit as st
import pandas as pd
st.title("Text input")
name=st.text_input("Enter your name")
age=st.slider("Select your age", 0, 100, 25)
opt=["Python", "Java", "C++", "Javascript"]
choice=st.selectbox("Choose your favorite lang:", opt)
st.write(f"Your fav lang is {choice}")
st.write(f"Your age is {age}.")
if name:
    st.write(f"Hello, {name}")

data={
    "Name":["Jhon", "Jane", "Jake", "Jill"],
    "Age":[28, 24, 35, 40],
    "City":["NY", "LA", "Cc", "HN"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

upload_file=st.file_uploader("Choose a csv file", type="csv")
if upload_file is not None:
    df1=pd.read_csv(upload_file)
    st.write("Your uploaded file in streamlit")
    st.write(df1)

