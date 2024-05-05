# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:38:24 2024

@author: Svenson
"""

import random
import matplotlib.pyplot as plt

def coin_flip_experiment(n):
    """
    Führt einen Münzwurfversuch mit n Durchführungen durch und gibt die Anzahl der Kopf- und Zahl-Ergebnisse zurück.

    Args:
        n (int): Die Anzahl der Durchführungen des Münzwurfversuchs.

    Returns:
        tuple: Ein Tupel (heads, tails) mit der Anzahl der Kopf- und Zahl-Ergebnisse.
    """
    # help(random.choice) liefert folgende erklärung:
        #Choose a random element from a non-empty sequence
        #result = random.choice(['Kopf', 'Zahl'])
        #liefert also ein zufälliges Ergebnis aus der gegebenen Liste
    
    return heads, tails

def plot_coin_flip_experiment(heads, tails):
    """
    Plottet die Ergebnisse eines Münzwurfversuchs.

    Args:
        heads (int): Die Anzahl der Kopf-Ergebnisse.
        tails (int): Die Anzahl der Zahl-Ergebnisse.
    """
    # TODO 

if __name__ == "__main__":
    # Anzahl der Durchführungen des Münzwurfversuchs
    n = 1000

    # Münzwurfversuch durchführen
    heads, tails = coin_flip_experiment(n)

    # Ergebnisse plotten
    plot_coin_flip_experiment(heads, tails)
