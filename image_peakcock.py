import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


st.set_page_config(page_title="peakcock", layout="wide")

st.title("Peakcock Image Processor - Multi-Color Channel Visualizer")

@st.cache_data
def load_image():
    url  = "https://tse2.mm.bing.net/th/id/OIP.-HIewbbK6yx5Fg6Xg5hofAHaE7?w=626&h=417&rs=1&pid=ImgDetMain&o=7&rm=3"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

Peacock = load_image()
st.image(Peacock, caption="Original Peacock Image", use_container_width=True)

Peacock_np = np.array(Peacock)
R, G, B = Peacock_np[:, :, 0], Peacock_np[:, :, 1],  Peacock_np[:, :, 2]

red_img = np.zeros_like(Peacock_np)
green_img = np.zeros_like(Peacock_np)
blue_img = np.zeros_like(Peacock_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)
    
with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)
    
with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)    
Peacock_gray = Peacock.convert("L")
Peacock_gray_np = np.array(Peacock_gray)


fig, ax = plt.subplots(figsize=(4,4))
im = ax.imshow(Peacock_gray_np, cmap=colormap)
plt.axis("off")

st.pyplot(fig)

