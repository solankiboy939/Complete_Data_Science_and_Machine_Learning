import pandas as pd
import streamlit as st

# File uploader
uploaded_file = st.file_uploader('Upload File', type=['csv', 'xlsx'])

# Initialize a session state to track if a file has been uploaded
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

# Read the uploaded file and update the session state
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    
    st.session_state.file_uploaded = True
    st.session_state.dataframe = df
    st.experimental_rerun()

# Display the dataframe and charts if a file has been uploaded
if st.session_state.file_uploaded:
    df = st.session_state.dataframe
    st.write(df)

    if not df.empty:
        st.subheader('Line Chart')
        st.line_chart(df, use_container_width=True)

        st.subheader("Area Chart")
        st.area_chart(df, use_container_width=True)

        st.subheader("Bar Chart")
        st.bar_chart(df, use_container_width=True)
else:
    st.info("Please upload a CSV or Excel file.")
