import streamlit as st
import pandas as pd

df= pd.read_csv("business_investments.csv")

#data at a glance 
st.dataframe(df.head())

st.title("Pizza.Com App")

st.header("Starter")

st.subheader("Mains")

st.subheader("Desserts")




# Using the "with" syntax declare a form and call methods
with st.form(key='login'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

col1, col2 = st.beta_columns(2)

with col1:
    with st.form('Form1'):
        st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
        st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
        submitted1 = st.form_submit_button('Submit 1')

with col2:
    with st.form('Form2'):
        st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
        st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
        submitted2 = st.form_submit_button('Submit 2')

