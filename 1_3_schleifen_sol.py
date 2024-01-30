# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:42:19 2024

@author: Sven
"""

# Beispielcode mit einer Schleife

# Eine Liste von Zahlen
zahlen = [1, 2, 3, 4, 5]

# Eine for-Schleife, um durch die Liste zu iterieren
for zahl in zahlen:
    quadrat = zahl ** 2
    print(f"Die Quadratzahl von {zahl} ist {quadrat}")

'''

Schreibe einen Code der die Fibonacci-Folge ausgibt.

'''
# Beispiel: Die ersten 10 Zahlen der Fibonacci-Folge
n = 10
fib_sequence = [0, 1]

for _ in range(2, n):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

result = fib_sequence

print(f"Die ersten {n} Zahlen der Fibonacci-Folge sind: {result}")