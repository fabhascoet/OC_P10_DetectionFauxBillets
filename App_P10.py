# Import des librairies Python
import numpy as np
import pandas as pd

# Import des librairies pour Streamlit
import streamlit as st
from PIL import Image # Import d'image

# Eléments de titre
st.subheader("Projet 10 : Détection de faux billets 💵")
image = Image.open('Logo.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("Application finale")

# Import du fichier à analyser (CSV)
data = st.file_uploader("Déposer les données à analyser")

print(data)
