import streamlit as st
from PIL import Image
import os
from facenet import FaceNet

st.set_page_config(
    page_title="Face Recognition",
    page_icon="🌞",
)

model = FaceNet('model.pt')

col1, col2 = st.columns(2)

col1.title('Face Recognition')

uploaded_file = col1.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    save_path = os.path.join("uploaded_images", uploaded_file.name)
    
    if not os.path.exists("uploaded_images"):
        os.makedirs("uploaded_images")

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = Image.open(save_path)
    name = model(save_path)
    col2.subheader(f'`{name}`')
    col2.image(image, caption="Uploaded Image", use_column_width=True, width=100)

else:
    col1.info("Please upload an image file.")