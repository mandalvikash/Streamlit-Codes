import streamlit as st

#Method 1
Page_config={"page_title":"JCharishTech","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**Page_config)

#method 2
#st.set_page_config(page_title='Hello',page_icon='😅',layout='wide',initial_sidebar_state='auto')

def main():
    st.title("Hello Streamlit lovers 😅😅")
    st.sidebar.success("Menu")

if __name__=='__main__':
    main()