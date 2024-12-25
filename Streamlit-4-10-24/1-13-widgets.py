import streamlit as st
name="Vikash"
if st.button("Submit"):
    st.write("Name:{}".format(name.upper()))


if st.button("Submit",key="01"):
    st.write("Name:{}".format(name.lower()))

status=st.radio("What is your status",("Active","Inactive"))
if status=='Active':
    st.success("You are active")
elif status=='Inactive':
    st.warning("You are inactive")


if st.checkbox("Show/Hide"):
    st.text("Showing something")

with st.expander("Python"):
    st.success("Hello Python")