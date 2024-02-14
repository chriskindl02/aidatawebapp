import streamlit as st
import openai
from typing import List
from streamlit_chat import message
import numpy as np
import pandas as pd





with st.chat_message("user"):
    st.write("Hello 👋")
    st.write("Hello human")
    uploaded_file = st.file_uploader("Bitte zu analysierende Datei hochladen",type=['xlsx','csv'],accept_multiple_files=False)
    main_data = "No Data selected"
    if uploaded_file is not None:
        st.write(uploaded_file.name)
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names
        selected_sheet=st.selectbox("select the sheet", sheet_names)
        df = pd.read_excel (uploaded_file, sheet_name=selected_sheet)
        main_data = df

    st.write(main_data)
        
    