import time
import numpy as np 
import pandas as pd 
import streamlit as st 

st.set_page_config(page_title="portfolio",page_icon="Teju",layout='wide')

#Spinner
with st.spinner("Wait for it"):
    time.sleep(15)
    st.write("Thanks for being patient")
    
#Progress Bar
with st.empty():
    for percent_completed in range(100):
        time.sleep(1)
        st.progress(percent_completed+1,text="Processing")
        st.success("Congratulations")
        
#Cool Stuff
st.balloons()
st.snow()