import numpy as np 
import pandas as pd
import streamlit as st 
import time

cases=[]

for _ in range(100):
    cases.append(np.random.randint(1,7))
data=[]
for i in range(1,7):
    data.append(cases.count(i))
    
st.header("Frequency of getting a Face")
st.bar_chart({"data":data})

with st.expander("See Explanation"):
    st.write("The Chart show some number I got from rolling a dics 100 times and its basically about how many times each face appears");
    st.image("https://static.streamlit.io/examples/dice.jpg")

with st.empty():
    st.write("You need to wait for 10 sec ")
    for sec in range(11):
        st.write(str(sec) +"seconds remained")
        time.sleep(1)
    st.write('10 sec completed')