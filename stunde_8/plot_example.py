# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:46:15 2024

@author: Svenson
"""

import matplotlib.pyplot as plt
import numpy as np

print('test')
input('test2')
# Daten für den Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Erstellen des Plots
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)')
plt.title('Sinus Funktion')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Speichern des Plots als Bild
plt.savefig('plot.png')

# Anzeigen des Plots
plt.show()
