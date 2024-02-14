import streamlit as st
import openai
from typing import List
from streamlit_chat import message
import numpy as np
import pandas as pd

main_data="empty"

st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.chat_message("user"):
    st.write("Hallo Nutzer👋")
    uploaded_file = st.file_uploader("Bitte lade die Datei hoch, die ich für dich analysieren soll:",type=['xlsx','csv'],accept_multiple_files=False)
    
    if uploaded_file is not None:
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names
        selected_sheet=st.selectbox("Bitte wähle das Tabellenblatt aus, welches ich für dich analysieren soll!", sheet_names)
        df = pd.read_excel (uploaded_file, sheet_name=selected_sheet)
        main_data =df
        st.write (main_data)
        
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")