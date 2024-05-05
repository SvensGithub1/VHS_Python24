def spielfeld_erstellen(zeilen, spalten):
    """
    Erstellt ein leeres Spielfeld mit der angegebenen Anzahl von Zeilen und Spalten.
    
    Args:
        zeilen (int): Die Anzahl der Zeilen im Spielfeld.
        spalten (int): Die Anzahl der Spalten im Spielfeld.
        
    Returns:
        list: Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
    """
    spielfeld = [[' ' for _ in range(spalten)] for _ in range(zeilen)]
    return spielfeld

def spielfeld_anzeigen(spielfeld):
    """
    Zeigt das aktuelle Spielfeld auf der Konsole an.
    
    Args:
        spielfeld (list): Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
    """
    for zeile in spielfeld:
        print("| " + " | ".join(zeile) + " |")
        print("+" + "---+" * len(zeile))

def spielstein_fallenlassen(spielfeld, spalte, spielstein):
    """
    Lässt einen Spielstein in die angegebene Spalte fallen.
    
    Args:
        spielfeld (list): Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
        spalte (int): Die Spalte, in die der Spielstein fallen gelassen werden soll.
        spielstein (str): Der Spielstein, der fallen gelassen werden soll ('X' oder 'O').
        
    Returns:
        bool: True, wenn der Spielstein erfolgreich platziert wurde, False sonst.
    """
    for zeile in range(len(spielfeld)-1, -1, -1):
        if spielfeld[zeile][spalte] == ' ':
            spielfeld[zeile][spalte] = spielstein
            return True
    return False

def ist_gewinner(spielfeld, spielstein):
    """
    Überprüft, ob der angegebene Spielstein gewonnen hat.
    
    Args:
        spielfeld (list): Ein zweidimensionales Listenobjekt, das das Spielfeld repräsentiert.
        spielstein (str): Der Spielstein, der überprüft werden soll ('X' oder 'O').
        
    Returns:
        bool: True, wenn der Spielstein gewonnen hat, False sonst.
    """
    # Horizontal prüfen
    for zeile in range(len(spielfeld)):
        for spalte in range(len(spielfeld[zeile])-3):
            if spielfeld[zeile][spalte] == spielstein and spielfeld[zeile][spalte+1] == spielstein and spielfeld[zeile][spalte+2] == spielstein and spielfeld[zeile][spalte+3] == spielstein:
                return True

    # Vertikal prüfen
    for zeile in range(len(spielfeld)-3):
        for spalte in range(len(spielfeld[zeile])):
            if spielfeld[zeile][spalte] == spielstein and spielfeld[zeile+1][spalte] == spielstein and spielfeld[zeile+2][spalte] == spielstein and spielfeld[zeile+3][spalte] == spielstein:
                return True

    # Positiv diagonale prüfen
    for zeile in range(len(spielfeld)-3):
        for spalte in range(len(spielfeld[zeile])-3):
            if spielfeld[zeile][spalte] == spielstein and spielfeld[zeile+1][spalte+1] == spielstein and spielfeld[zeile+2][spalte+2] == spielstein and spielfeld[zeile+3][spalte+3] == spielstein:
                return True

    # Negativ diagonale prüfen
    for zeile in range(3, len(spielfeld)):
        for spalte in range(len(spielfeld[zeile])-3):
            if spielfeld[zeile][spalte] == spielstein and spielfeld[zeile-1][spalte+1] == spielstein and spielfeld[zeile-2][spalte+2] == spielstein and spielfeld[zeile-3][spalte+3] == spielstein:
                return True

    return False

def get_valid_column_choice(spalten):
    """
    Fragt den Benutzer nach einer gültigen Spaltennummer und gibt sie zurück.
    
    Args:
        spalten (int): Die Anzahl der Spalten im Spielfeld.
        
    Returns:
        int: Die vom Benutzer gewählte Spaltennummer.
    """
    while True:
        try:
            spalte = int(input(f"Wähle eine Spalte (0-{spalten-1}): "))
            if 0 <= spalte < spalten:
                return spalte
            else:
                print("Ungültige Spalte! Bitte eine Zahl zwischen 0 und", spalten-1, "eingeben.")
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

def main():
    """
    Hauptfunktion des Vier-Gewinnt-Spiels.
    """
    zeilen = 6
    spalten = 7
    spielfeld = spielfeld_erstellen(zeilen, spalten)
    spiel_beendet = False
    zug = 0

    while not spiel_beendet:
        spielfeld_anzeigen(spielfeld)
        if zug % 2 == 0:
            spielstein = 'X'
        else:
            spielstein = 'O'

        spalte = get_valid_column_choice(spalten)

        if spielstein_fallenlassen(spielfeld, spalte, spielstein):
            if ist_gewinner(spielfeld, spielstein):
                spielfeld_anzeigen(spielfeld)
                print(f"Spieler {spielstein} gewinnt!")
                spiel_beendet = True
            elif ' ' not in spielfeld[0]:
                spielfeld_anzeigen(spielfeld)
                print("Unentschieden!")
                spiel_beendet = True
            zug += 1
        else:
            print("Spalte ist voll. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
