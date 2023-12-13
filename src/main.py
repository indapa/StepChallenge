import streamlit as st
import pandas as pd
from pathlib import Path

import streamlit as st
st.set_page_config(layout="wide")

default_data = Path(__file__).parent.parent /  "Data" / "steps.csv"


tab1, tab2, tab3= st.tabs(["Introduction", "Benefits of Walking", "Tips for Success"])

with tab1:
   st.header("1 Million Step Challenge")

   st.markdown("""
               
               Join me in my effort to walk 1 million steps in the first 100 days of 2024! That's taking 10,000 steps a day for 100 days!
               
               I've made this app to help me track my progress and keep me motivated. I hope you'll join me in this challenge!

               See this [link](https://docs.google.com/spreadsheets/d/1Gbk39PpU0Ec_bZCs3MnQyTyT_AdhN54TApCMEKY2wy4/edit?usp=sharing) to download a log to track your steps.


               Upload your step count data to plot and visualize your progress.

               """)

   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

   with st.form("my_form"):
     #file csv upload
      uploaded_file = st.file_uploader("Choose a file", type='csv')
      submitted = st.form_submit_button("Submit")
      if submitted:
         df = pd.read_csv(uploaded_file)
         st.write(df)
      else:
         df = pd.read_csv(default_data)
         st.write(df)

with tab2:
   st.header("Benefits of Walking")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

