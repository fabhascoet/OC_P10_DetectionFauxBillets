# Import des librairies Python
import numpy as np
import pandas as pd
import os
#import matplotlib.pyplot as plt

# Import des librairies pour Streamlit
import streamlit as st
from PIL import Image # Import d'image

# Eléments de titre
st.subheader("Projet 10 : Détection de faux billets 💵")
image = Image.open('Logo.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("Application finale")
# Import du fichier à analyser (CSV)
#data = st.file_uploader("Déposer les données à analyser")
#import os
#st.dataframe(data)

# Import du fichier à analyser (CSV)
#data = st.file_uploader("Déposer les données à analyser", type=["csv"])
#if data is not None:
    #st.dataframe(data)
    #data.info()
#else:
    #st.write("Aucun fichier déposé")

#display(data)
#data.info()

#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
#for uploaded_file in uploaded_files:
    #bytes_data = uploaded_file.read()
    #st.write("filename:", uploaded_file.name)
    #st.write(bytes_data)

    
uploaded_file = st.file_uploader("Choose a file")
# Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)
