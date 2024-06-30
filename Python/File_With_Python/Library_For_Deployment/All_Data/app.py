import pandas as pd
import streamlit as st
import time
# from mymodel  import mymodel as m
st.title("Welcome To Edudrag! ")
# st.write(m.run(window = 15))
st.header("This is Header")
st.subheader("This is subheader")
st.write("""
#My first App
Hello *world!*
""")
st.text("This is for paragraph")
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')
st.success("Success")
st.info("Information!")
st.warning('warning!')
st.error('Error')
# st.radio(['mele','female']:['mele','female'])
st.code("x = 2021")
st.caption("This is caption")
st.latex(r'''
         a  + a r^1 a r^2 + a r^3''')
st.audio("ala.mp3")
st.video("video.mp4")
st.subheader("Are You Here!")
st.checkbox('Yes')
st.checkbox('No')
st.button("Submit")
st.radio('pick your gender',['Male','Female'])
st.multiselect('Choose a subject',['Machine Learning','Data Science', 'Full Stack Developer','Interner of thing', 
                                   'Software testing', 'Cloud Coumputing'])
st.select_slider('pick a mark',['Bad', 'Good', 'Excellent'])
st.slider('pick a number',0,50)
st.number_input('Pick a number',0,10)
st.text_input('Email adress')
st.date_input('Travelling Date')
st.time_input("College Time")
st.text_area('Descrpiption')
st.file_uploader('Upload a photo')
st.color_picker('choose your favorite color')
st.subheader('Progress')
st.progress(50)
st.balloons()
st.subheader('Wait the execution')
st.sidebar.title("Welcom to Edudrag!")
st.sidebar.button('Login')

# This is a sideBar Start!
option = st.sidebar.selectbox('Choose a Choice',['Select','login','Register'])
if(option == 'login'):
    st.sidebar.text_input("Enter Name:")
    st.sidebar.text_input("Enter Password",type = 'password')
elif(option == 'Register'):
    st.sidebar.text_input("Enter Name:")
    st.sidebar.text_input("Enter Email Id")
    password1 = st.sidebar.text_input("Enter the password",type = 'password')
    password2 = st.sidebar.text_input("confirm Password",type = 'password')
    if(password1 == password2):
        st.sidebar.markdown("Same Password!")
    else:
        st.sidebar.markdown("Password Not Same")
# st.sidebar.radio('pick a gender',['Male','Female'])

# SideBar End!


# with st.spinner('Wait for it......'):
#     time.sleep(5)
#     st.success('Success')

from streamlit_pdf_viewer import pdf_viewer


container_pdf, container_chat = st.columns([50, 50])


with container_pdf:
    pdf_file = st.file_uploader("Upload PDF file", type=('pdf'))

    if pdf_file:
        binary_data = pdf_file.getvalue()
        pdf_viewer(input=binary_data,
                   width=700)

st.header("Uplading CSV File:")
df = st.file_uploader("Upload Csv File",type = ['csv','xlsx'])
if df is not None:
    st.dataframe(df)
    
