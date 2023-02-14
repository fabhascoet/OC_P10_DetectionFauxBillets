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

st.write("Données d'entrainement")

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("This is tab 1")


# Import du fichier à analyser (CSV)
uploaded_xtrain = st.file_uploader("Déposer les données d'entrainement (X)")
if uploaded_xtrain is not None:
    X_train = pd.read_csv(uploaded_xtrain)
else:
    st.write("Aucun fichier déposé")

tab2.write("This is tab 2")
# Import du fichier à analyser (CSV)
uploaded_ytrain = st.file_uploader("Déposer les données d'entrainement (Y)")
if uploaded_ytrain is not None:
    y_train = pd.read_csv(uploaded_ytrain)
else:
    st.write("Aucun fichier déposé")

    
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

