# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:45:47 2024

@author: Svenson
"""

def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Beispiel: Die ersten 10 Zahlen der Fibonacci-Folge
n = 10
result = fibonacci(n)

print(f"Die ersten {n} Zahlen der Fibonacci-Folge sind: {result}")