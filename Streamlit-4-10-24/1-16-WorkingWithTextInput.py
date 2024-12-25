import streamlit as st
fname=st.text_input("Enter first name:")
st.title(fname)

#password
password=st.text_input("Enter password",type="password")


#For bigger size of input box
message=st.text_area("Enter message",height=300)
st.write(message)

#for number input
number=st.number_input("Enter Number",1,25)
st.write(number)

#date input
my_appoinment=st.date_input("Appoinment Date")
st.write(my_appoinment)

#Time input
myTime=st.time_input("My Time")
st.write(myTime)

#color input
color=st.color_picker("Select Color")