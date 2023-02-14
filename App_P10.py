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
st.subheader("Application finale")
image = Image.open('Logo.jpg')
st.image(image, caption='Logo ONCFM')


# Section pour importer les données d'entrainement
st.subheader("Données d'entrainement")

# Création de 2 onglets dans la section
tab1, tab2 = st.tabs(["X", "Y"])

# Informations de la 1ère section
# Import du fichier à analyser (CSV)
uploaded_xtrain = tab1.file_uploader("Déposer les données d'entrainement (X)")
if uploaded_xtrain is not None:
    X_train = pd.read_csv(uploaded_xtrain)
else:
    tab1.write("Aucun fichier déposé pour les données d'entrainements (X)")

# Informations de la 2nde section
# Import du fichier à analyser (CSV)
uploaded_ytrain = tab2.file_uploader("Déposer les données d'entrainement (Y)")
if uploaded_ytrain is not None:
    y_train = pd.read_csv(uploaded_ytrain)
else:
    tab2.write("Aucun fichier déposé pour les données d'entrainements (Y)")


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

