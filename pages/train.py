import streamlit as st
import zipfile
import io
import os

from facenet import FaceNet 

model = FaceNet()

st.set_page_config(
    page_title="Train",
    page_icon="🚀",
)



col1, col2 = st.columns(2)

col1.title("Train")

uploaded_file = col1.file_uploader("Choose a zip file", type="zip")

def unzip_file(uploaded_file,extract_to="dataset"):
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        return os.path.abspath(extract_to)

DATASET_PATH = ''            

if uploaded_file is not None:
    try:
        DATASET_PATH = unzip_file(uploaded_file)
        col1.success("File unzipped successfully!")
    except zipfile.BadZipFile:
        col1.error("Invalid zip file!")
else:
    col1.info("Please upload a zip file.")
    

def train():
    model.train()
    

if col1.button("train"):
    model.train(DATASET_PATH)
    col1.success("model trained successfully!")
    


col2.title('File structure')
col2.markdown('class1')
col2.markdown('├── image1.jpg')
col2.markdown('└── image2.jpg')
col2.markdown('class2')
col2.markdown('├── image1.jpg')
col2.markdown('└── image2.jpg')

