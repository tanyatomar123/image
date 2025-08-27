# app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit page setup
st.set_page_config(page_title="Image Processing App", layout="centered")

st.title("🖼️ Image Processing with Streamlit")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image with OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Resize to 1080x720
    img_resized = cv2.resize(img, (1080, 720))

    # Convert for display (BGR → RGB)
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    st.image(img_rgb, caption="Resized Image (1080x720)", use_container_width=True)

    # Buttons for actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Gray"):
            gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
            st.image(gray, caption="Grayscale Image", use_container_width=True)

    with col2:
        if st.button("Blur"):
            blur = cv2.GaussianBlur(img_resized, (15, 15), 0)
            blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
            st.image(blur_rgb, caption="Blurred Image", use_container_width=True)

    with col3:
        if st.button("Edge"):
            edges = cv2.Canny(img_resized, 100, 200)
            st.image(edges, caption="Edge Detection", use_container_width=True)
