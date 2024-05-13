# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:39:18 2024

@author: Svenson
"""

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except #überlege welche exception hier ausgeworfen werden könnte

# Testen der Funktion
print(read_file('sample.txt'))        # Ausgabe: Inhalt der 'sample.txt'-Datei
