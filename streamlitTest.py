import streamlit as st
import pandas as pd
import numpy as np

st.title('Test 123')

st.write("TEST")

st.sidebar.header('This is the sidebar')
st.sidebar.markdown("""
                    **This is *the* sidebar markdown**
                    - oh yeah
                    - it works
                    
                    """)

file = st.sidebar.file_uploader('Upload a CSV file', type=['csv'])
if file is not None:
    df = pd.read_csv(file)
st.dataframe(df)

st.sidebar.selectbox("TEST", ["Option 1", "Option 2", "Option 3"])
st.sidebar.slider("TEST", 0, 100, 50)
st.sidebar.text_input("TEST", "Type here...")

