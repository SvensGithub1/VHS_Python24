# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:49:00 2024

@author: Sven
"""
import time
import random
from numba import jit
#%% sortier eine Liste von Integern nach der Größe
def bubble_sort(arr):
    n = len(arr)
    # Durchläuft alle Elemente der Liste
    for i in range(n):
        # Letzte i Elemente sind bereits sortiert, daher j bis n-i-1
        for j in range(0, n-i-1):
            # Vergleiche benachbarte Elemente und tausche, falls notwendig
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
def partition(arr, low, high):
    # Wähle das letzte Element als Pivot
    pivot = arr[high]
    # Index des kleineren Elements
    i = low - 1
    
    for j in range(low, high):
        # Wenn das aktuelle Element kleiner oder gleich dem Pivot ist
        if arr[j] <= pivot:
            # Inkrementiere den Index des kleineren Elements
            i += 1
            # Tausche arr[i] und arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Tausche arr[i+1] und arr[high] (Pivot)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi ist der Index, an dem das Pivot-Element liegt
        pi = partition(arr, low, high)
        
        # Rekursiv sortiere die beiden Teile
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
def is_sorted(arr):
    # Überprüft, ob das Array sortiert ist
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def random_sort(arr):
    '''
    This sort is called Bogosort.

    Best case is O(n): your first shuffle returned a sorted list. If this happens for any decently sized list, you should probably buy a lottery ticket.
    Average case is O((n+1)!)
    Worst case is unbounded. There's no guarantee that the random shuffling will ever return a sorted list. It is random after all.

    Parameters
    ----------
    arr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # Solange das Array nicht sortiert ist, mische es zufällig
    while not is_sorted(arr):
        random.shuffle(arr)
@jit(nopython=True, cache=True)
#Numba is a just-in-time compiler for Python  
def bubble_sort2(arr):
    n = len(arr)
    # Durchläuft alle Elemente der Liste
    for i in range(n):
        # Letzte i Elemente sind bereits sortiert, daher j bis n-i-1
        for j in range(0, n-i-1):
            # Vergleiche benachbarte Elemente und tausche, falls notwendig
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]   
        
if __name__ == "__main__":


    random_integers = [random.randint(1, 100) for _ in range(10000)]
    #print(random_integers)
    t0 = time.time()
    random_integers.sort()
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
    
    random_integers = [random.randint(1, 100) for _ in range(10000)]
    t0 = time.time()
    bubble_sort(random_integers)
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
    
    random_integers = [random.randint(1, 100) for _ in range(10000)]
    t0 = time.time()
    bubble_sort2(random_integers)
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
    
    random_integers = [random.randint(1, 100) for _ in range(10000)]
    t0 = time.time()
    quick_sort(random_integers, 0, len(random_integers)-1)
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
    
    random_integers = [random.randint(1, 100) for _ in range(10)]
    t0 = time.time()
    random_sort(random_integers)
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
