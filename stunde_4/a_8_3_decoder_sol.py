# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:54:42 2024

@author: Sven
"""

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('Z'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext

def main():
    with open("encrypted_text.txt", "r") as file:
        ciphertext = file.read()
    shift = int(input("Geben Sie die Verschiebungszahl ein: "))
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print("Entschlüsselter Text:", decrypted_text)

if __name__ == "__main__":
    main()
