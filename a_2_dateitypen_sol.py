# -*- coding: utf-8 -*-

das_ist_ein_string = "Inhalt"
das_auch = 'test'
zusammengefuehrt = das_ist_ein_string + ' ' + das_auch
print(zusammengefuehrt)

#%% Integer
das_ist_ein_integer = 3
#Rechenoperationen
addieren = 3 + 3
print(addieren)
subtrahieren = 3 - 3
print(subtrahieren)
multiplizieren = 3 * 3
print(multiplizieren)
dividieren = 3 / 3
exponenten = 3^3
print(exponenten)
addieren = 3 + das_ist_ein_integer
#%% Float

kommazahl = 3.14

#%% Listen
teilnehmer = ['Max', 'Moritz']

print(teilnehmer)

#erstes Item
print(teilnehmer[0])

#letztes item
print(teilnehmer[-1])

#anhängen
teilnehmer.append('Vanessa')
print(teilnehmer)

#entfernen
teilnehmer.pop(1)
print(teilnehmer)
#%% schreibt ein Liste für ein Rezept für Pfannkuchen entfernt eine Zutat unf fügt eine neue hinzu
pfannkuchen = ['Mehl', 'Milch', 'Eier', 'Öl']
print(pfannkuchen)
pfannkuchen.pop(-1)
pfannkuchen.append('Margarine')
print(pfannkuchen)

#%% dictionary (Wörterbuch)
autofarbe = {'VW': 'grün', 'Skoda': 'geld', 'Toyota': 1}
print(autofarbe)
print('Die Farbe des VWs ist ' + autofarbe['VW'] + '.')
#new value
autofarbe['Audi'] = 'schwarz'
print(type(autofarbe))

#%% Boolean
wahr = True
falsch = False
print(type(wahr))

