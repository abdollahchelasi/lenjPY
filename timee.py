import time
import streamlit as st

while True:

  # Load and run your actual Streamlit app
  import app

  time.sleep(60) 
  st.experimental_rerun()
