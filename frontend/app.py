import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Data Cleaner", layout='wide')
st.title("-*-*- Data Cleaning & Profiling Tool -*-*-")
file=st.file_uploader("Upload your CSV file", type=["csv"])

option=st.selectbox("Select Operation",["Profile Data", "Detect Issues", "Clean Data"])
if file:
    st.success("File uploaded successfully")
    #Showing Preview
    df=pd.read_csv(file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    file.seek(0)
    if st.button("Run"):
        with st.spinner("Processing..."):
            if option=="Profile Data":
                url="http://127.0.0.1:5000/profile"
            elif option=="Detect Issues":
                url="http://127.0.0.1:5000/issues"
            else:
                url="http://127.0.0.1:5000/clean"
            response=requests.post(url,files={"file":file})

            if response.status_code==200:
                result=response.json()
                st.subheader("Result")
                st.json(result)
            else:
                st.error(f"Error: {response.text}")