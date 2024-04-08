# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:39:38 2024

@author: Svenson
"""

#%% dictionary (Wörterbuch)
autofarbe = {'VW': 'grün', 'Skoda': 'geld', 'Toyota': 1}
print(autofarbe)
print('Die Farbe des VWs ist ' + autofarbe['VW'] + '.')
#new value
autofarbe['Audi'] = 'schwarz'
print(type(autofarbe))
