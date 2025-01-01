import numpy as np
import streamlit as st 
import pandas as pd

def Profile():
    with st.sidebar:
        st.title("Profile")
        
       

Profile()


    
#static 
col1,col2,col3=st.columns(3)
with col1:
    st.header("Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg",width=200)
with col2:
    st.header("Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
#Dynamic
n=st.number_input("How many columns do you want?",1,10)
cols=st.columns(n)
for col in cols:
    with col:
        st.image("https://static.streamlit.io/examples/cat.jpg",width=200)
        

#tab

tab1,tab2,tab3=st.tabs(["Cat","Dog","Owl"])
tab1.image("https://static.streamlit.io/examples/cat.jpg",width=200)
tab2.image("https://static.streamlit.io/examples/dog.jpg",width=200)
tab3.image("https://static.streamlit.io/examples/owl.jpg",width=200)

#dynamic tab
#imgs=pd.read_csv("/User/ashishzangra/Documents/Streamlit/imgs.csv")['img_link']
imgs=["https://static.streamlit.io/examples/cat.jpg","https://static.streamlit.io/examples/dog.jpg","https://static.streamlit.io/examples/owl.jpg"]
#tabs=st.tabs(['ID']*30)
tabs=st.tabs(["Cat","Dog","Owl"])
for tab in tabs:
    img=imgs[np.random.randint(1,3)]
    tab.image(img,width=400)



    