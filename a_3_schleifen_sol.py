# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:42:19 2024

@author: Sven
"""
#%% if statement
if True:
    print('wahr')
    
if False:
    print('falsch')
elif True:
    print('alternative')
else:
    print('zweite alternative')
   
#weitere test Bedingungen
nummer = 5
if nummer == 5:
    print('gleich 5')
if nummer != 4:
    print('ungleich 4')
'''
equals x == 42
not equal x != 42 
greater than x > 42 
equal to x >= 42
less than x < 42 
or equal to x <= 42
'''

#%% rechnen von user input
zahl_1 = input('Erste Zahl eingeben:')
operation = input('Bitte Rechenoperation eingeben:')
zahl_2 = input('Zweite Zahl eingeben:')

print(type(zahl_1))
zahl_1 = int(zahl_1)
zahl_2 = int(zahl_2)
print(type(zahl_1))
if operation == '+':
    print(zahl_1 + zahl_2 )
elif operation == '-':
    print(zahl_1 + zahl_2 )

#%% Ticketpreis berechnen
alter = int(input("Bitte geben Sie Ihr Alter ein: "))
schueler = input("Sind Sie ein Schüler? (ja/nein): ")

if schueler == "ja":
    schueler = True
else:
    schueler = False

if alter < 6:
    preis = 0
elif 6 <= alter <= 17:
    if schueler:
        preis = 5
    else:
        preis = 10
else:
    preis = 12

print("Der Eintrittspreis beträgt:", preis, "Euro.")
#%% Alternative
zahl = 6
schueler = 'ja'
if zahl >= 5 and schueler == 'ja':
    print('Größer 5 und Schüler.')
'''
Ähnliche Verwendung von:
    and not
    or
'''

#%% Alternative Ticketpreis berechnen
alter = int(input("Bitte geben Sie Ihr Alter ein: "))
schueler = input("Sind Sie ein Schüler? (ja/nein): ")

if schueler == "ja":
    schueler = True
else:
    schueler = False

if alter < 6:
    preis = 0
elif 6 <= alter <= 17 and schueler:
    preis = 5
elif 6 <= alter <= 17 and not schueler:
    preis = 10
else:
    preis = 12

print("Der Eintrittspreis beträgt:", preis, "Euro.")
#%% schleifen
# Beispielcode mit einer Schleife

# Eine Liste von Zahlen
zahlen = [1, 2, 3, 4, 5]

# Eine for-Schleife, um durch die Liste zu iterieren
for zahl in zahlen:
    quadrat = zahl ** 2
    print(f"Die Quadratzahl von {zahl} ist {quadrat}")
    
#%% alternative schleife
zahlen = [1, 2, 3, 4, 5]

# Eine for-Schleife, um durch die Liste zu iterieren
for zahl in range((len(zahlen))):
    quadrat = zahl ** 2
    print(f"Die Quadratzahl von {zahl} ist {quadrat}")

'''

Schreibe einen Code der die Fibonacci-Folge ausgibt.

'''
#%% Beispiel: Die ersten 10 Zahlen der Fibonacci-Folge
n = 10
fib_sequence = [0, 1]

for _ in range(2, n):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

result = fib_sequence

print(f"Die ersten {n} Zahlen der Fibonacci-Folge sind: {result}")
#%% while Schleibe
# Initialisierung der Obergrenze
obergrenze = 5
# Initialisierung der Summe
summe = 0
# Initialisierung der Zählvariable
zahl = 1

# while-Schleife zur Berechnung der Summe
while zahl <= obergrenze:
    print(zahl)
    summe += zahl
    zahl += 1
# theoretisch Fibonacci-Folge auch mit while Schleife bestimmen
# %% break statement
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
else:
    print("wird nur ausgeführt wenn keine 3 vorhanden")
#%% switch case
response_code = 201
match response_code:
     case 200:
         print("OK")
     case 201:
         print("Created")
     case 300:
         print("Multiple Choices")
     case 307:
         print("Temporary Redirect")
     case 404:
         print("404 Not Found")
     case 500:
         print("Internal Server Error")
     case 502:
         print("502 Bad Gateway")
