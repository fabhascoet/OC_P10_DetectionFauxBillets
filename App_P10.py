import streamlit as st
import numpy as np
import pandas as pd

# Eléments de titre
st.subheader("Projet 10 : Détection de faux billets 💵")

from PIL import Image

image = Image.open('Logo.jpg')

st.image(image, caption='Sunrise by the mountains')

st.write("Application finale")

# Sidebar pour import des données
st.sidebar.write("Importer les données à analyser")
st.sidebar.button("Click me!")



#st.write("Download button - Display a download button widget")
#st.download_button("Download file", file)

#st.write("File Uploader - Display a file uploader widget")
#data = st.file_uploader("Upload a CSV")

