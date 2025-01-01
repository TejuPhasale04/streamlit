import streamlit as st 

def rate_yourself():
    with st.sidebar:
        st.title("Rate Yourself")
        lang=st.text_input("Enter the programming you know with comma sepration",value="Python")
        lang=[i.strip() for i in lang.split(',')]
        
        st.subheader('How would you rate your experience in the following programming and tools?')
        
        for l in lang:
            st.write(l)
            st.slider(l,min_value=0.,max_value=10.,step=0.5)


                
            
            
rate_yourself()
