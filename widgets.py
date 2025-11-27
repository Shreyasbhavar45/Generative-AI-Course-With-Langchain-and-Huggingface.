import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name =st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)
st.write(f"your age is {age}.")

options = ["python","Java","c++","Javascript"]
choice = st.selectbox("choose your favourite language:",options)
st.write(f"you selected{choice}.")

if name :
    st.write(f"Hello,{name}")

data = {
    "name" : ["John","jane","jake","jilli"],
    "Age"  : [28,24,35,40],
    "city" : ["Nashik","Pune","Mumbai","Yeola"]
}   

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files = st.file_uploader("choose a csv file",type = "csv")

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)
   
