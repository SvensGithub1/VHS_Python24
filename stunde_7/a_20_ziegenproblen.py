import random
import matplotlib.pyplot as plt

def ziegenproblem():
    """
    Simuliert das Ziegenproblem und gibt aus, ob der Spieler gewonnen hat, wenn er die Tür wechselt oder nicht.

    Returns:
        bool: True, wenn der Spieler gewinnt, wenn er die Tür wechselt, False sonst.
    """
    # Wähle zufällig eine Tür, hinter der sich der Preis befindet
    price_door = random.randint(1, 3)

    # TODO
    
    return win, switch

if __name__ == "__main__":
    # Anzahl der Durchführungen des Zufallsexperiments
    experiments = 10000
    switch_wins = 0
    stay_wins = 0
    # Anzahl der Siege, wenn der Spieler die Tür wechselt
    for _ in range(experiments):
        win, switch = ziegenproblem()
        if switch and win:
            switch_wins += 1
        elif win:
            stay_wins += 1
    


    # Ergebnisse plotten
    # TODO 