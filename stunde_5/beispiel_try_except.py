# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:47:08 2024

@author: Svenson
"""

try:
    zahl = int(input("Bitte gib eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Das Ergebnis ist:", ergebnis)
except ZeroDivisionError:
    print("Du kannst nicht durch Null teilen!")
except ValueError:
    print("Das war keine gültige Zahl!")


# allgemeiner 

try:
    zahl = int(input("Bitte gib eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Das Ergebnis ist:", ergebnis)
except Exception as e:
    # Code, der ausgeführt wird, wenn eine Ausnahme auftritt
    print("Ein Fehler ist aufgetreten:", e)