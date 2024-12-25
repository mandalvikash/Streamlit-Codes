import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv("file.csv")
pd.set_option("styler.render.max_elements", 289674)

# st.dataframe(df)
# st.dataframe(df,200,100)

# st.table(df)
num_cols = df.select_dtypes(include=[np.number])
st.dataframe(num_cols.style.highlight_max(axis=0))

st.write(df.head())

st.json({'data':'name'})

mycode="""
def sayHello():
    print("Hello Streamlit")
end
    """
st.code(mycode,language='python')