# Import des librairies Python
import numpy as np
import pandas as pd
import os
# Import des librairies pour Streamlit
import streamlit as st
from PIL import Image # Import d'image

# Eléments de titre
st.subheader("Projet 10 : Détection de faux billets 💵")
st.subheader("Application finale")
image = Image.open('Logo.jpg')
st.image(image, caption='Logo ONCFM')


## Section 1 : importer les données d'entrainement

# Titre
st.subheader("Données d'entrainement")

# Création de 2 onglets dans la section
tab1, tab2 = st.tabs(["X", "Y"])

# Informations de la 1ère section
# Import du fichier à analyser (CSV)
uploaded_xtrain = tab1.file_uploader("Déposer les données d'entrainement (X)")
if uploaded_xtrain is not None:
    X_train = pd.read_csv(uploaded_xtrain)
    tab1.success("Données chargées X !")
else:
    tab1.warning("Aucun fichier déposé pour les données d'entrainements (X)")

# Informations de la 2nde section
# Import du fichier à analyser (CSV)
uploaded_ytrain = tab2.file_uploader("Déposer les données d'entrainement (Y)")
if uploaded_ytrain is not None:
    y_train = pd.read_csv(uploaded_ytrain)
    tab2.success("Données chargées y !")
else:
    tab2.warning("Aucun fichier déposé pour les données d'entrainements (Y)")


## Section 2 : importer les nouvelles données

# Titre
st.subheader("Nouvelles données à analyser")

# Import du fichier à analyser (CSV)
uploaded_file = st.file_uploader("Déposer les données à analyser")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.success("Données à analyser chargées !")
else:
    st.warning("Aucun fichier déposé pour les nouvelles données")

    
## Section 3 : Préparation des données

# Création dataframe pour les prédictions sans la colonne ID
New_billets_predict= dataframe.drop("id", axis=1)
# Enregistrement des ID dans un dataframe
ID = dataframe["id"]


## Section 4 : Entraînement du modèle
from sklearn.linear_model import LogisticRegression
# On choisit "LogisticRegression"
model_lrg = LogisticRegression()
# Entraînement du modèle sur les données
model_lrg.fit(uploaded_xtrain, uploaded_ytrain)

