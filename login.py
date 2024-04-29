import streamlit as st
import mysql.connector
from multiple_disease_prediction_system import show_main_page
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages



def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uservalidation"
    )


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def authenticate(username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "SELECT * FROM validation WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = authenticate(username, password)
        if user:
            st.session_state.user = user
            st.success("Login successful!")
            sleep(0.5)
            st.switch_page("multiple_disease_prediction_system.py")
        else:
            st.error("Invalid username or password. Please try again.")


        
with st.sidebar:
       if 'user' in st.session_state:
           st.subheader('We Care Hospitals')
           st.title('Where Care Meets Compassion')
           st.write("Welcome, ", st.session_state.user[0]) 
           st.write("---")
           
           
