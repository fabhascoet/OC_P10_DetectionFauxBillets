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


import csv

nom_fichier = "https://github.com/fabhascoet/OC_P10_DetectionFauxBillets/blob/main/X_rlg_train.csv" # À remplacer par le chemin vers le fichier :)

# Contenu supposé du fichier :
# 1;2;3
# a;b

fp = open(nom_fichier, "r", encoding="utf-8")
for ligne in csv.reader(fp, delimiter=";"):
    for cellule in ligne:
        print(cellule)
    print("Fin de ligne")
# [Sortie] 1
# [Sortie] 2
# [Sortie] 3
# [Sortie] Fin de ligne
# [Sortie] a
# [Sortie] b
# [Sortie] Fin de ligne


# Choix de l'estimateur
#model_lrg = LogisticRegression()
# Entrainement du modèle
#model_lrg.fit(X_rlg_train, y_rlg_train)


## Prédictions
# Importation du modèle de prédiction
#url = "https://github.com/fabhascoet/OC_P10_DetectionFauxBillets/blob/main/modele_reg_log.sav"
#df = pd.read_spss(url)
#pip install --upgrade joblib
#from joblib import load


# Load the model from the file
#model = load("model_lrg.joblib")


# ouverture en lecture binaire
#f = open("modele_reg_log.sav", "rb")
# et chargement
#model_lrg = pickle.load(f)
# fermeture du fichier
#f.close()
