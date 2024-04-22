# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:03:57 2024

@author: Svenson
"""

import time
import random

#%% sortier eine Liste von Integern nach der Größe
def dein_sort(arr):
    #führe help(list) aus um die Dokumentation der Listen zu bekommen. 
    # dies erklärt auch entsprechenden Funktionen
    '''
    

    Parameters
    ----------
    arr : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    zwischenspeicher = arr[0]
    sortiert = []
    for ii in arr:
        if zwischenspeicher > ii:
            zwischenspeicher = ii 
    sortiert.append(zwischenspeicher)
    arr.remove(zwischenspeicher)
    print(sortiert)
    return sortiert

if __name__ == "__main__":


    random_integers = [random.randint(1, 100) for _ in range(100)]
    #print(random_integers)
    t0 = time.time()
    random_integers.sort()
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)
    
    random_integers = [random.randint(1, 100) for _ in range(100)]
    t0 = time.time()
    dein_sort(random_integers)
    t1 = time.time()
    #print(random_integers)
    total = t1-t0
    print(total)