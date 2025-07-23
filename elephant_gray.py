import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Function to load image from a URL
def load_image_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensures error is raised for bad response
    return Image.open(BytesIO(response.content))

# Image URL
elephant_url = "https://th.bing.com/th/id/R.e1d0ec7162f7405c6cb53a90e92ab641?rik=tq7zCaRpciz9aw&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f3%2f37%2fAfrican_Bush_Elephant.jpg&ehk=tGht%2fLxzX62nMSANAMx%2blAtQIDN787mnVToJKqn2APw%3d&risl=1&pid=ImgRaw&r=0"

# Load the image
elephant = load_image_from_url(elephant_url)

# Display original image
plt.figure(figsize=(6, 4))
plt.imshow(elephant)
plt.title("Elephant")
plt.axis("off")
plt.show()

# Convert to grayscale
elephant_gray = elephant.convert("L")

# Display grayscale image
plt.figure(figsize=(6, 4))
plt.imshow(elephant_gray, cmap="gray")
plt.title("Elephant - Grayscale")
plt.axis("off")
plt.show()