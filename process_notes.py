# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:28:16 2024

@author: etudiant
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_data(filepath):
    data = np.loadtxt(filepath)
    return data

def calculate_statistics(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return mean, std_dev

def plot_data(data):
    # Création de la figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Calcul de l'histogramme des données
    hist, bins = np.histogram(data, bins=10)
    
    # Calcul des positions de départ pour les barres (x, y, z)
    xpos = bins[:-1]  # Positions de départ sur l'axe x
    ypos = np.zeros_like(xpos)  # Toutes les barres commencent à y = 0
    zpos = np.zeros_like(xpos)  # Toutes les barres commencent à z = 0

    # Dimensions des barres
    dx = np.ones_like(hist) * (bins[1] - bins[0])  # Largeur des barres
    dy = np.ones_like(hist) * 0.5  # Profondeur des barres arbitraire
    dz = hist  # Hauteur des barres selon les comptages d'histogramme

    # Ajout des barres au graphique
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

    # Afficher le graphique
    plt.show()

def main():
    try:
        data = load_data("FilteredNotes.txt")
        mean, std_dev = calculate_statistics(data)
        print(f"Moyenne: {mean:.2f}, Écart type: {std_dev:.2f}")
        plot_data(data)
    except Exception as e:
        print(f"Erreur: {str(e)}")

if __name__ == "__main__":
    main()
