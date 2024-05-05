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

    # Spieler wählt zufällig eine Tür
    player_choice = random.randint(1, 3)

    # Monty Hall öffnet eine Tür, die weder die vom Spieler gewählte Tür noch die mit dem Preis ist
    doors = [1, 2, 3]
    doors.remove(price_door)
    if player_choice in doors:
        doors.remove(player_choice)
    opened_door = random.choice(doors)

    # Spieler entscheidet, ob er die Tür wechseln möchte oder nicht
    switch = random.choice([True, False])

    # Wenn der Spieler wechselt, wählt er eine der verbleibenden Türen außer seiner ursprünglichen Wahl und der geöffneten Tür
    if switch:
        doors = [1, 2, 3]
        doors.remove(player_choice)
        doors.remove(opened_door)
        player_choice = doors[0]

    # Überprüfen, ob der Spieler die Tür mit dem Preis gewählt hat
    win = player_choice == price_door
    
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
    labels = ['Gewinne','Wechseln', 'Nicht Wechseln']
    sizes = [switch_wins + stay_wins, switch_wins, stay_wins]
    colors = ['lightcoral', 'lightblue', 'lightgreen']

    plt.bar(labels, sizes, color=colors)
    plt.xlabel('Strategie des Spielers')
    plt.ylabel('Anzahl der Siege')
    plt.title('Ergebnisse des Ziegenproblems')
    plt.show()
