# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:32:00 2024

@author: Svenson
"""
'''
Römische Zahlen werden durch sieben verschiedene Symbole dargestellt: I, V, X, L, C, D und M.

Symbol Wert
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Zum Beispiel wird die Zahl 2 als II in römischen Zahlen geschrieben, einfach zwei Einsen addiert. Die Zahl 12 wird als XII geschrieben, was einfach X + II ist. Die Zahl 27 wird als XXVII geschrieben, was XX + V + II ist.

Römische Zahlen werden normalerweise von links nach rechts in absteigender Reihenfolge geschrieben. Die Zahl vier wird jedoch nicht als IIII geschrieben. Stattdessen wird die Zahl vier als IV geschrieben. Weil die Eins vor der Fünf steht, ziehen wir sie ab und erhalten vier. Das gleiche Prinzip gilt für die Zahl neun, die als IX geschrieben wird. Es gibt sechs Fälle, in denen Subtraktion verwendet wird:

I kann vor V (5) und X (10) platziert werden, um 4 und 9 zu bilden.
X kann vor L (50) und C (100) platziert werden, um 40 und 90 zu bilden.
C kann vor D (500) und M (1000) platziert werden, um 400 und 900 zu bilden.

Gegeben eine römische Zahl, konvertiere sie in eine ganze Zahl.

Beispiel 1:

Eingabe: s = "III"
Ausgabe: 3
Erklärung: III = 3.
Beispiel 2:

Eingabe: s = "LVIII"
Ausgabe: 58
Erklärung: L = 50, V= 5, III = 3.
Beispiel 3:

Eingabe: s = "MCMXCIV"
Ausgabe: 1994
Erklärung: M = 1000, CM = 900, XC = 90 und IV = 4.
''' 

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        