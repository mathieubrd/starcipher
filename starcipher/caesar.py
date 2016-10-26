import re

# Utility class to encrypt, decrypt and crack messages using the Caesar cipher.
class Caesar:

    # Encrypts the given message with the given key.
    # Returns the encrypted message.
    def encrypt(key, message):
        chars = list(message.upper())
        for i in range(0, len(chars)):
            if re.compile('[A-Z]').match(chars[i]):
                chars[i] = chr((ord(chars[i]) - 65 + key) % 26 + 65)
        return "".join(chars)

    # Decrypts the given message using the given key.
    # Returns the potentially decrypted message.
    def decrypt(key, message):
        chars = list(message.upper())
        for i in range(0, len(chars)):
            if (re.compile('[A-Z]').match(chars[i])):
                chars[i] = chr((ord(chars[i]) - 65 - key) % 26 + 65)
        message = "".join(chars)
        return message

    # Does a frequency analysis on the given message.
    # Returns a dictionnary containing the frequency of each letter in the given message.
    def frequencies(message):
        frequencies = {}
        num_letters = 0;
        for char in message.upper():
            if re.compile('[A-Z]').match(char):
                num_letters += 1
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1;
        for letter, frequency in frequencies.items():
            frequencies[letter] = round(frequencies[letter] / num_letters * 100, 2)
        return frequencies

    # Crack the given message using the brute force method.
    # Returns the potentially cracked message or None if there is no match.
    def brute_force(message, dict):
        for i in range(1, 26):
            message_tmp = Caesar.decrypt(i, message)
            if dict.recognize(message_tmp) > 0.6:
                return message_tmp
        return None
