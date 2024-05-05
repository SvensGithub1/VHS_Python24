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
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden!")
        return None
    except PermissionError:
        print(f"Sie haben keine Berechtigung, die Datei '{file_path}' zu lesen!")
        return None

# Testen der Funktion
print(read_file('sample.txt'))        # Ausgabe: Inhalt der 'sample.txt'-Datei
print(read_file('nonexistent_file.txt')) # Ausgabe: Die Datei 'nonexistent_file.txt' wurde nicht gefunden!
print(read_file('hier_koennte_eine Datei_stehen_bei_dem_die_berechtigungen_feheln'))       # Ausgabe: Sie haben keine Berechtigung, die Datei '/etc/shadow' zu lesen!
