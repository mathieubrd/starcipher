import re

# Utility class to encrypt, decrypt and crack messages using the Vigenere cipher.
class Vigenere:

    # Encrypts the given message using the given key.
    # Returns the encrypted message.
    def encrypt(key, message):
        if len(key) < 1:
            raise 'Vigenere cipher needs a key.'
        key = list(key.upper())
        message = list(message.upper())
        key_index = 0
        for i in range(0, len(message)):
            if re.compile('[A-Z]').match(message[i]):
                key_ord = ord(key[key_index % len(key)])
                char_ord = ord(message[i])
                message[i] = chr((key_ord + char_ord) % 26 + 65)
                key_index += 1
        return ''.join(message)

    # Decrypts the given message using the given key.
    # Returns the potentially decrypted message.
    def decrypt(key, message):
        if len(key) < 1:
            raise 'Vigenere cipher needs a key.'
        key = list(key.upper())
        message = list(message.upper())
        key_index = 0
        for i in range(0, len(message)):
            if re.compile('[A-Z]').match(message[i]):
                key_ord = ord(key[key_index % len(key)])
                char_ord = ord(message[i])
                message[i] = chr((char_ord - key_ord) % 26 + 65)
                key_index += 1
        return ''.join(message)

    # Cracks the given message using the given dictionnary.
    # Returns the potentially decrypted message or None if there is no match.
    def crack(dict, message):
        return None
