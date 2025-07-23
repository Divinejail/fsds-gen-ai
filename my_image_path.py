import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aditya Image Processor", layout="wide")

st.title("Aditya Image -Multi - Color channel Visualizer")

@st.cache_data
def load_image():
    path = r"C:\Users\adity\OneDrive\Desktop\photos\me.jpg" 
    return Image.open(path).convert("RGB")

Aditya = load_image()
st.image(Aditya, caption="Orignal Aditya Image", use_container_width=True)


Aditya_np = np.array(Aditya)
R, G, B = Aditya_np[:, :, 0], Aditya_np[:, :, 1], Aditya_np[:, :, 2]

red_img = np.zeros_like(Aditya_np)
green_img = np.zeros_like(Aditya_np)
blue_img = np.zeros_like(Aditya_np)

red_img[:, : , 0] = R
green_img[:, :, 1]= G
blue_img[:, :, 2]= B

st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width= True)
    
with col2:
    st.image(green_img, caption="Green Channel", use_container_width= True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)
    

st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

Aditya_gray = Aditya.convert("L")
Aditya_gray_np = np.array(Aditya_gray)


fig, ax = plt.subplots(figsize=(4,4))
im = ax.imshow(Aditya_gray_np, cmap=colormap)
plt.axis("off")

st.pyplot(fig)