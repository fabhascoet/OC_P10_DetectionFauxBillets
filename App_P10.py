# Import des librairies Python
import numpy as np
import pandas as pd
import os
# Import matplotlib.pyplot as plt
import pickle # Librairie chargement du modèle

# Import des librairies pour Streamlit
import streamlit as st
from PIL import Image # Import d'image

# Eléments de titre
st.subheader("Projet 10 : Détection de faux billets 💵")
image = Image.open('Logo.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("Application finale")

# Import du fichier à analyser (CSV)
uploaded_file = st.file_uploader("Déposer les données à analyser")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
else:
    st.write("Aucun fichier déposé")

## Préparation des données
# Création dataframe pour les prédictions sans la colonne ID
# Billets_predict= dataframe.drop("id", axis=1)
# Enregistrement des ID dans un dataframe
# ID = dataframe["id"]

#X_train="https://github.com/fabhascoet/OC_P10_DetectionFauxBillets/blob/main/X_rlg_train.csv"
#Xtrain = pd.read_csv(X_train)
#Xtrain = pd.read_csv("C:/Users/hasco/OneDrive/Documents/OC_Notebooks_Jupyter/Projet 10/Mission\Data/X_rlg_train.csv")
url = "https://github.com/fabhascoet/OC_P10_DetectionFauxBillets/blob/main/X_rlg_train.csv"
df = pd.read_csv(url)
