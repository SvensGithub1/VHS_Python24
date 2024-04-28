import unittest

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

class TestCaesarEncoder(unittest.TestCase):
    def test_encode_with_positive_shift(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_encode_with_negative_shift(self):
        self.assertEqual(caesar_encrypt("Hello, World!", -3), "Ebiil, Tloia!")

    def test_encode_with_zero_shift(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 0), "Hello, World!")

    def test_encode_with_large_shift(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 27), "Ifmmp, Xpsme!")

    def test_encode_with_non_alpha_characters(self):
        self.assertEqual(caesar_encrypt("Hello, World! 123", 3), "Khoor, Zruog! 123")


if __name__ == "__main__":
    #main()
    unittest.main()
    assert caesar_encrypt("Hello, World!", 3) == "Khoor, Zruog!"
    