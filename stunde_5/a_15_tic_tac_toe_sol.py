# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:42:49 2024

@author: Sven
"""

def spielfeld_erstellen():
    """
    Erstellt ein leeres 3x3 Tic-Tac-Toe-Spielfeld.
    
    Returns:
        list: Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
    """
    return [[' ' for _ in range(3)] for _ in range(3)]

def spielfeld_anzeigen(spielfeld):
    """
    Zeigt das aktuelle Tic-Tac-Toe-Spielfeld auf der Konsole an.
    
    Args:
        spielfeld (list): Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
    """
    for zeile in spielfeld:
        print("| " + " | ".join(zeile) + " |")
        print("+" + "---+" * len(zeile))

def ist_gewinner(spielfeld, spieler):
    """
    Überprüft, ob der angegebene Spieler gewonnen hat.
    
    Args:
        spielfeld (list): Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
        spieler (str): Der Spieler, der überprüft werden soll ('X' oder 'O').
        
    Returns:
        bool: True, wenn der Spieler gewonnen hat, False sonst.
    """
    # Horizontal und vertikal prüfen
    for i in range(3):
        if all(spielfeld[i][j] == spieler for j in range(3)) or all(spielfeld[j][i] == spieler for j in range(3)):
            return True
    
    # Diagonal prüfen
    if all(spielfeld[i][i] == spieler for i in range(3)) or all(spielfeld[i][2-i] == spieler for i in range(3)):
        return True

    return False

def get_valid_move():
    """
    Fragt den Benutzer nach gültigen Koordinaten für seinen Zug und gibt sie zurück.
    
    Returns:
        tuple: Die Koordinaten (Zeile, Spalte) des gültigen Zugs.
    """
    while True:
        try:
            eingabe = input("Gib deine Koordinaten im Format 'Zeile Spalte' ein (z.B. '1 2'): ")
            zeile, spalte = map(int, eingabe.split())
            if 1 <= zeile <= 3 and 1 <= spalte <= 3:
                return zeile - 1, spalte - 1
            else:
                print("Ungültige Koordinaten! Bitte Zahlen zwischen 1 und 3 eingeben.")
        except ValueError:
            print("Ungültige Eingabe! Bitte Zahlen im richtigen Format eingeben.")

def main():
    """
    Hauptfunktion des Tic-Tac-Toe-Spiels.
    """
    spielfeld = spielfeld_erstellen()
    spieler = 'X'
    zug = 0

    while True:
        spielfeld_anzeigen(spielfeld)
        print(f"Spieler {spieler} ist dran.")
        zeile, spalte = get_valid_move()

        if spielfeld[zeile][spalte] == ' ':
            spielfeld[zeile][spalte] = spieler
            if ist_gewinner(spielfeld, spieler):
                spielfeld_anzeigen(spielfeld)
                print(f"Spieler {spieler} hat gewonnen!")
                break
            elif zug == 8:
                spielfeld_anzeigen(spielfeld)
                print("Unentschieden!")
                break
            spieler = 'O' if spieler == 'X' else 'X'
            zug += 1
        else:
            print("Feld bereits belegt. Bitte einen anderen Zug wählen.")

if __name__ == "__main__":
    main()
