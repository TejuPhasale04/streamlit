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

def calBMI():
    with st.form(key='BMI Calculator',clear_on_submit=False):
        col1,col2,col3=st.columns([3,2,1])
        with col1:
            weight=st.number_input("Enter your weight in KGS")
        with col2:
            height=st.number_input("Enter your height in mtrs")
        with col3:
            submit=st.form_submit_button(label='Calculate')

    if submit:
        try:
            BMI=round((weight/height**2),2)
        except:
            st.write("Divide by 0 error")
        if BMI <=18.5:
            st.error("Underweight")
        elif 18.5 < BMI < 24.9:
            st.success("Healthy/Normal BMI")
        elif 25 <= BMI <=29.9:
            st.warning("Overweight")
        elif BMI >=30.0:
            st.error("OBESE")
                
            
            
rate_yourself()

calBMI()