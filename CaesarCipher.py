class CaesarCipher():
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''
    
    def encrypt(self, message, key):
        encrypted_message = []
        for char in message:
            encrypted_letter_index = self.letters.index(char.upper()) + key
            if encrypted_letter_index > 25:
                encrypted_letter_index %= 26
            encrypted_message.append(self.letters[encrypted_letter_index])
        self.translated = ''.join(encrypted_message)
        return self.translated
    def decrypt(self, message, key):
        decrypted_message = []
        for char in message:
            decrypted_letter_index = self.letters.index(char.upper()) - key
            if decrypted_letter_index < 0:
                decrypted_letter_index += 26
            decrypted_message.append(self.letters[decrypted_letter_index])
        self.translated = ''.join(decrypted_message)
        return self.translated
if __name__ == "__main__":
    cipher = CaesarCipher()
    print(cipher.encrypt("HELLO", 3))