

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
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