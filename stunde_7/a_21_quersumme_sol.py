# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:12:04 2024

@author: Sven


Gegeben eine ganze Zahl num, addiere wiederholt alle ihre Ziffern, bis das Ergebnis nur noch eine Ziffer hat, und gib es zurück.

Beispiel 1:

Eingabe: num = 38
Ausgabe: 2
Erklärung: Der Prozess ist
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Da 2 nur eine Ziffer hat, gib sie zurück.
Beispiel 2:

Eingabe: num = 0
Ausgabe: 0


"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num < 10):
            return num
        else:
            return self.addDigits(num//10 + num %10)