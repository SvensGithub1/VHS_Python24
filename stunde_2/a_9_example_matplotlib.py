# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:23:07 2024

@author: Svenson
"""

import matplotlib.pyplot as plt
import numpy as np

#cheatsheets https://matplotlib.org/cheatsheets/

#%% 
# Daten für den Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot erstellen
plt.plot(x, y)

# Beschriftungen hinzufügen
plt.title('Einfacher Linienplot')
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')

# Plot anzeigen
plt.show()

#%% Streudiargramm

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot erstellen
plt.scatter(x, y, color='red')

# Beschriftungen hinzufügen
plt.title('Streudiagramm')
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')

# Plot anzeigen
plt.show()

#%% balkendiagramm
# Daten für den Plot
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 15]

# Plot erstellen
plt.bar(categories, values, color='green')

# Beschriftungen hinzufügen
plt.title('Balkendiagramm')
plt.xlabel('Kategorien')
plt.ylabel('Werte')

# Plot anzeigen
plt.show()

#%% Histogramm 
# Zufällige Daten generieren
data = np.random.randn(1000)

# Histogramm erstellen
fig, ax = plt.subplots()
ax.hist(data, bins=30, color='orange')

# Beschriftungen hinzufügen
ax.set_title('Histogramm')
ax.set_xlabel('Werte')
ax.set_ylabel('Häufigkeit')

# Plot speichern
plt.savefig('histo.svg')
