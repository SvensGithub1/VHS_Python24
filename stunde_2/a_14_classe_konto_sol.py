# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:18:09 2024

@author: Sven
"""

class Konto(object): 

    def __init__(self, inhaber, kontonummer, 
                 kontostand, 
                 kontokorrent=0): 
        self.__Inhaber = inhaber 
        self.__Kontonummer = kontonummer 
        self.__Kontostand = kontostand 
        self.__Kontokorrent = kontokorrent

    def ueberweisen(self, ziel, betrag):
        if(self.__Kontostand - betrag < -self.__Kontokorrent):
            # Deckung nicht genuegend
            return False  
        else: 
            self.__Kontostand -= betrag 
            ziel.__Kontostand += betrag 
            return True
 
    def einzahlen(self, betrag): 
       self.__Kontostand += betrag 
 
    def auszahlen(self, betrag): 
       self.__Kontostand -= betrag 
 
    def get_kontostand(self): 
        return self.__Kontostand
    

K1 = Konto("Jens",70711,2022.17)
K2 = Konto("Uta",70813,879.09)
K1.kontostand()
K1.ueberweisen(K2,998.32)
print(K1.get_kontostand())

print(K2.get_kontostand())
