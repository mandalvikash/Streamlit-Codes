import streamlit as st
my_lang=["Python","Julia","Go","Rust"]

#single select
choice=st.selectbox("Language",my_lang)
st.write("You selected {} ".format(choice))

#multiple select
spoken_lang=("English","Hindi","French","Spanish")
my_spoken_lang=st.multiselect("Spoken Language",spoken_lang,default="English")
st.write("You selected {}".format(my_spoken_lang))


#slider
age=st.slider("Age",1,100)

#select slider
#Number(Int/Float/Dates)
color=st.select_slider("Choose Color",options=["Yellow","Red","Green","Blue"])