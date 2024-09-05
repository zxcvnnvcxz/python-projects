import streamlit as st
from PIL import Image

# Upload image from computer
upload_image = st.file_uploader("Upload Image")
if upload_image:
    img = Image.open(upload_image)
    gray_img = img.convert("L")
    st.image(gray_img)

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to greyscale
    gray_img = img.convert("L")

    # Render the greyscale image on the website
    st.image(gray_img)