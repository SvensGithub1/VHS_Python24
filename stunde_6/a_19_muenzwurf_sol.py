import random
import matplotlib.pyplot as plt

def coin_flip_experiment(n):
    """
    Führt einen Münzwurfversuch mit n Durchführungen durch und gibt die Anzahl der Kopf- und Zahl-Ergebnisse zurück.

    Args:
        n (int): Die Anzahl der Durchführungen des Münzwurfversuchs.

    Returns:
        tuple: Ein Tupel (heads, tails) mit der Anzahl der Kopf- und Zahl-Ergebnisse.
    """
    heads = 0
    tails = 0

    for _ in range(n):
        result = random.choice(['Kopf', 'Zahl'])
        if result == 'Kopf':
            heads += 1
        else:
            tails += 1
    
    return heads, tails

def plot_coin_flip_experiment(heads, tails):
    """
    Plottet die Ergebnisse eines Münzwurfversuchs.

    Args:
        heads (int): Die Anzahl der Kopf-Ergebnisse.
        tails (int): Die Anzahl der Zahl-Ergebnisse.
    """
    labels = ['Kopf', 'Zahl']
    sizes = [heads, tails]
    colors = ['gold', 'lightcoral']
    explode = (0.1, 0)  # Betonung des Kopf-Ergebnisses

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Ergebnisse des Münzwurfversuchs')
    plt.show()

if __name__ == "__main__":
    # Anzahl der Durchführungen des Münzwurfversuchs
    n = 1000

    # Münzwurfversuch durchführen
    heads, tails = coin_flip_experiment(n)

    # Ergebnisse plotten
    plot_coin_flip_experiment(heads, tails)
