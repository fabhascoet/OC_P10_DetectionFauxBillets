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

## Données à analyser
# Import du fichier à analyser (CSV)
uploaded_file = st.file_uploader("Choose a file")
# Transformation dataframe à partir du CSV
dataframe = pd.read_csv(uploaded_file)
# Affiche le dataframe
st.write(dataframe)

## Préparation des données
# Création dataframe pour les prédictions sans la colonne ID
Billets_predict= dataframe.drop("id", axis=1)
# Enregistrement des ID dans un dataframe
ID = dataframe["id"]

df = pd.read_spss("https://github.com/fabhascoet/OC_P10_DetectionFauxBillets/blob/main/modele_reg_log.sav")



## Prédictions
# Importation du modèle de prédiction

# ouverture en lecture binaire
#f = open("modele_reg_log.sav", "rb")
# et chargement
#model_lrg = pickle.load(f)
# fermeture du fichier
#f.close()
