import streamlit as st

st.title("Pizza.com App")


# Using the "with" syntax declare a form and call methods
with st.sidebar.form(key='login'):
    st.header("Log in")
    st.write("*Log into your account to save your order details.*")
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
    
st.header("Starter")
st.write("Select your starter choice.")
st.radio('Pick one', ['Nachos', 'Garlic bread'])

st.subheader("Mains")

col1, col2 = st.beta_columns(2)
with col1:
    with st.form('Form1'):
        st.write("Select heat level.\n\n 0= Xtra Mild.")
        st.slider(label='Select your preferred heat intensity level', min_value=0, step=2, max_value=10, key='4')
        submitted1 = st.form_submit_button('Submit')
        
with col2:
    with st.form('Form2'):
        st.selectbox('Select Base', ['Classic thin crust', 'Stuffed crust'], key='2')
        submitted2 = st.form_submit_button('Submit')

st.subheader("Desserts")
st.write("Choose what dessert you would like.")
st.multiselect('Chocolate cake with', ['vanilla ice-cream','custard','chocolate sauce'])

st.header("Delivery details")
st.write("Enter your delivery address below")
st.text_area('Enter Text Here!')
st.button('Click if you would like utensils')
st.time_input("What time would you like your order to be delivered?")







