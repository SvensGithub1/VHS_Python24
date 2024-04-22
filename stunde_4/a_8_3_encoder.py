# ein ist Funktion zu schreiben die einen Text nach dem Caeser Cipher verschlüsseln soll
# Erklärung https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung
# dafür verwendet ihr am besten den Datentyp char:
   #Char oder Character ist ein Datentyp (in vielen Programmiersprachen) für 
    # Datenbereiche/Felder, deren Elemente jeweils ein Zeichen repräsentieren.
    #
    # also nur a oder b oder 1 oder A 

# um den ceasar cipher ausführen zu können müssen die buchstaben in den Zahlenraum transpomiert werden.
# Das geschieht wie folgt:
    
# Die Funktion »chr« ergibt eine Zeichenfolge mit genau einem Zeichen, welches die als Argumentwert übergebene Kennzahl hat.

#Auswertung
print(chr( 65 ))
print(chr( ord( 'A' )+ 1 ))
# ihr könnt am anfang davon ausgehen das nur groß- oder kleinbuchstaben vorhanden sind.

def caesar_encrypt(plaintext, shift):
    '''
    

    Parameters
    ----------
    plaintext : Sting
        Text der verschlüsselt werden soll.
    shift : Int
        Anzahl an schritten um die verschlüsselt werden soll.

    Returns
    -------
    ciphertext : string
        verschlüsselter text.

    '''
    ciphertext = ""
    for char in plaintext:
        #TODO eine Funktion schrieben die den plaintext verschlüsselt

    return ciphertext

def main():
    plaintext = input("Geben Sie den zu verschlüsselnden Text ein: ")
    shift = int(input("Geben Sie die Verschiebungszahl ein: "))
    encrypted_text = caesar_encrypt(plaintext, shift)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)
    print("Verschlüsselter Text wurde in 'encrypted_text.txt' gespeichert.")

if __name__ == "__main__":
    main()