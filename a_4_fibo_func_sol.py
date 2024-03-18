# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:45:47 2024

@author: Sven
"""

def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence
    
def fibonacci_rec(n, fib_sequence = [0,1]):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)
    if n > len(fib_sequence):
        fib_sequence = fibonacci_rec(n, fib_sequence)
    return fib_sequence
if __name__ == "__main__":
     # execute only if run as a script
     # Beispiel: Die ersten 10 Zahlen der Fibonacci-Folge
     n = 10
     result = fibonacci(n)
    
     print(f"Die ersten {n} Zahlen der Fibonacci-Folge sind: {result}")
     
     n = 10
     result = fibonacci_rec(n)
    
     print(f"Die ersten {n} Zahlen der Fibonacci-Folge sind: {result}")