# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:18:09 2024

@author: Sven
"""

class Konto(object): 

    def __init__(self, inhaber, kontonummer, 
                 kontostand, 
                 kontokorrent=0): 
        # TODO init definieren
        
        
    def ueberweisen(self, ziel, betrag):
        '''
        # TODO überweisen von diesem konto auf ein Ziel Konto.
        Check of genügend geld auf konto
        

        Parameters
        ----------
        ziel : TYPE
            DESCRIPTION.
        betrag : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        
        
 
    def einzahlen(self, betrag): 
       '''
       TODO 
       Funktion zum Einzahlen

        Parameters
        ----------
        betrag : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
 
    def auszahlen(self, betrag): 
       '''
        TODO Funktion zum auszahlen schreiben

        Parameters
        ----------
        betrag : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
 
    def get_kontostand(self): 
        '''
        Kontostand ausgeben

        Returns
        -------
        None.

        '''
    

K1 = Konto("Jens",70711,2022.17)
K2 = Konto("Uta",70813,879.09)
print(K1.kontostand())
print(K1.ueberweisen(K2,998.32))
print(K1.kontostand())

print(K2.kontostand())
