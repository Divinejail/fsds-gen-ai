
import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Aditya Image Processor", layout="wide")

# Title
st.title("Aditya Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    url = "https://tse1.mm.bing.net/th/id/OIP.LQZpQ_gRrC6l0LusvOGUwgHaJW?rs=1&pid=ImgDetMain&o=7&rm=3"  # this  is for url
    # path = r"C:\Users\adity\OneDrive\Desktop\photos\me.jpg"
    response = requests.get(url)  # this  is for url
    return Image.open(BytesIO(response.content)).convert("RGB")   # this  is for url
    # return Image.open(path).convert("RGB")

# Load and display image
Aditya = load_image()
st.image(Aditya, caption="Original Aditya Image", use_container_width=True)

# Convert to NumPy array
Aditya_np = np.array(Aditya)
R, G, B = Aditya_np[:, :, 0], Aditya_np[:, :, 1], Aditya_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(Aditya_np)
green_img = np.zeros_like(Aditya_np)
blue_img = np.zeros_like(Aditya_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

Aditya_gray = Aditya.convert("L")
Aditya_gray_np = np.array(Aditya_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(4   , 4))
im = ax.imshow(Aditya_gray_np, cmap=colormap)
plt.axis("off")

# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)