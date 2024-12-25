import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
def main():
    st.title("Ploting in streamlit with plotly")
    df = pd.read_csv("C:\\Users\\vikas\\OneDrive\\Desktop\\STREAMLIT\\Streamlit-4-10-24\\updated_pollution_dataset.csv")

    st.dataframe(df)
    fig=px.pie(df,values='Temperature',names='Air Quality',title='Pie Chart')
    st.plotly_chart(fig)

    fig2=px.bar(df,x="Air Quality",y='Temperature')
    st.plotly_chart(fig2)
if __name__=='__main__':
    main()

