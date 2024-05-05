'''
Erstelle eine Klasse Fahrrad. Die Instanzen dieser Klasse sollen folgende Attribute besitzen:

eine Zeichenkette __marke (private): das Attribut beschreibt die Marke des Fahrrads

eine positive ganze Zahl __anz_zahnkraenze (private): diese Attribut beschreibt die Anzahl Zahnkränze des Fahrrads.

eine positive ganze Zahl __anz_ritzel (private): diese Attribut beschreibt die Anzahl Ritzel des Fahrrads.

eine positive ganze Zahl _zahnkranz (protected): diese Attribut beschreibt den gegenwärtige Zahnkranz des Fahrrads.

eine positive ganze Zahl _ritzel (protected): diese Attribut beschreibt das gegenwärtige Ritzel des Fahrrads.

Ausserdem soll die Klasse folgenden Methoden besitzen:

get_marke(): gibt die Marke zurück.

get_anz_zahnkraenze(): gibt die Anzahl Zahnkränze zurück.

get_anz_ritzel(): gibt die Anzahl Ritzel zurück.

get_zahnkranz(): gibt den gegenwärtigen Zahnkranz zurück.

get_ritzel(): gibt das gegenwärtige Ritzel zurück.

up_zahnkranz(): verschiebt die Kette über den nächsten Zahnkranz (wenn möglich).

down_zahnkranz(): verschiebt die Kette über den vorherigen Zahnkranz (wenn möglich).

up_ritzel(): verschiebt die Kette über das nächste Ritzel (wenn möglich).

down_ritzel(): verschiebt die Kette über das vorherigen Ritzel (wenn möglich).

print_zustand(): gibt den gegenwärtigen Zustand des Fahrrads in folgender Form:
'''

class Fahrrad:
    
    def __init__(self, marke, anz_zahnkraenze, anz_ritzel, zahnkranz, ritzel):
        self.__marke = marke
        self.__anz_zahnkraenze = anz_zahnkraenze
        self.__anz_ritzel = anz_ritzel
        self._zahnkranz = zahnkranz
        self._ritzel = ritzel
    
    def get_marke(self):
        return self.__marke
    
    def get_anz_zahnkraenze(self):
        return self.__anz_zahnkraenze
    
    def get_anz_ritzel(self):
        return self.__anz_ritzel
    
    def get_zahnkranz(self):
        return self._zahnkranz
    
    def get_ritzel(self):
        return self._ritzel
    
    def up_zahnkranz(self):
        if (self.get_zahnkranz() < self.get_anz_zahnkraenze()):
            self._zahnkranz += 1 # x += 1 ist äquivalent zu x = x + 1
    
    def down_zahnkranz(self):
        if (self.get_zahnkranz() > 1):
            self._zahnkranz -= 1
    
    def up_ritzel(self):
        if (self.get_ritzel() < self.get_anz_ritzel()):
            self._ritzel += 1
    
    def down_ritzel(self):
        if (self.get_ritzel() > 1):
            self._ritzel -= 1
            
    def print_zustand(self):
        print(self.get_marke(), end = " ")
        for i in range(self.get_anz_zahnkraenze()):
            if i == self.get_zahnkranz() - 1:
                print("*", end = "")
            else:
                print("o", end = "")
        print("----", end = "")
        for i in range(self.get_anz_ritzel()):
            if i == self.get_ritzel() - 1:
                print("*", end = "")
            else: print("o", end = "")    
        print()


if __name__ == "__main__":
    f = Fahrrad("Mountain Bike", 3, 10, 2, 5)
    f.print_zustand()
    f.up_ritzel()
    f.print_zustand()
    f.up_zahnkranz()
    f.up_zahnkranz()
    f.print_zustand()
    f.down_zahnkranz()
    f.up_ritzel()
    f.up_ritzel()
    f.up_ritzel()
    f.up_ritzel()
    f.print_zustand()
    f.down_zahnkranz()
    f.down_ritzel()
    f.down_ritzel()
    f.down_ritzel()
    f.print_zustand()
    f.down_zahnkranz()
    f.print_zustand()
    f.down_zahnkranz()
    f.print_zustand()
    g = Fahrrad("Mein Velo", 2, 5, 1, 1)
    g.print_zustand()
    print(g.get_marke(), "hat", g.get_anz_ritzel(), "Ritzel und", g.get_anz_zahnkraenze(), "Zahnkränze")

