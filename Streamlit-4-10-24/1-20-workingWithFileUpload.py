import streamlit as st
import pandas as pd

from PIL import Image
def load_image(image_file):
    img=Image.open(image_file)
    return img

def main():
    st.title("File Upload Tutorial")
    menu=["Home","Dataset","DoucmentFiles","About"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Home":
        st.subheader("Home")
        image_file=st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
        if image_file is not None:
           file_details = {"Filename": image_file.name, "FileType": image_file.type, "FileSize": image_file.size}
           st.write(file_details)
           st.image(load_image(image_file))
        else:
            st.write("Image is not uploaded yet")
    elif choice=="Dataset":
        st.subheader("Dataset")
        dataset_file=st.file_uploader("Upload Dataset",type=["CSV"])
        if st.button("Process"):
            if dataset_file is not None:
                dataset_details = {"Filename": dataset_file.name, "FileType": dataset_file.type, "FileSize": dataset_file.size}
                st.write(dataset_details)
                df=pd.read_csv(dataset_file)
                st.dataframe(df)
            else:
                st.write("Dataset not uploaded yet")
    elif choice=="DoucmentFiles":
        st.subheader("DoucmentFiles")
        docx_file=st.file_uploader("Upload Documents",type=["pdf","docx","txt"])
        if st.button("Process"):
            if docx_file is not None:
                document_details = {"Filename": docx_file.name, "FileType": docx_file.type, "FileSize": docx_file.size}
                st.write(document_details)
                if docx_file.type=="text/plan":
                    raw_text=docx_file.read()
    else:
        st.subheader("About")

if __name__=='__main__':
    main()