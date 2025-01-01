import streamlit as st
import datetime

st.subheader("Introduction Form:") 
name=st.text_input("Enter Your Name:",value="Tejaswini Phasale")
st.write("Welcome",name)

user_feedback=st.text_area("Provide Your Feedback:")
st.write("Your Feedback:",user_feedback)

age=st.number_input("Enter Your Age:",min_value=0,max_value=120,value=20)
st.write("Your Age:",age)

selected_date=st.date_input("Enter Your Date of Birth::",datetime.date.today())
st.write("Selected date:",selected_date)

gender=['ML','Data Analysis','AI']
select_gender=st.selectbox("Selet Your Gender:",gender,help="Choose One")
st.write("Your gender:",select_gender)

gender=st.radio("Select Your gender:",options=("Male","Female","other"),help="choose one",horizontal=True)
st.write("Your gender:",gender)

option=st.multiselect("Select Your options:",options=("Data Analysis","ML","DL","AI"),help="Choose One",default="Data Analysis")

if st.button('Say Hello'):
    st.write("Hi")
    
if st.checkbox("Iagree to term and condition",help="'You must agree to proced"):
    st.write("Thank you for agreeing")

color=st.color_picker("Selec your favourite color:",'#DC1D07')
st.write("You have selected",color,'color')

st.button("Submit You response")
