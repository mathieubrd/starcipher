import re

# Utility class to encrypt, decrypt and crack messages using affine cipher.
class Affine:

    # Returns True if the number passed in a prime number.
    def is_prime(n):
        for i in range(2, n):
            return pow(i, n - 1) % n == 1
        return True

    # Returns the Bézout coefficients and the gcd of the two given numbers.
    def xgcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = Affine.xgcd(b % a, a)
            return (g, y - (b // a) * x, x)

    # Returns the modular multiplicative inverse of n mod m
    def mod_inv(n, m):
        g, x, _ = Affine.xgcd(n, m)
        if g == 1:
            return x % m

    # Encrypt the a given message using the two given keys.
    # The first key must be coprime with 26 (the length of the alphabet).
    # Returns the encrypted message.
    def encrypt(key1, key2, message):
        if not Affine.is_prime(key1):
            raise Exception('First key must be a prime number.')
        message = list(message.upper())
        for i in range(0, len(message)):
            if re.compile('[A-Z]').match(message[i]):
                message[i] = chr(((key1 * (ord(message[i]) - 65) + key2) % 26) + 65)
        return "".join(message)

    # Decrypt (if it is possible) the given message using the two given keys.
    # Returns the potentially decrypted message.
    def decrypt(key1, key2, message):
        k = Affine.mod_inv(key1, 26)
        message = list(message.upper())
        for i in range(0, len(message)):
            if re.compile('[A-Z]').match(message[i]):
                message[i] = chr((k * (ord(message[i]) - key2 - 65) % 26) + 65)
        return ''.join(message)

    # Cracks the given message using the brute force method with the given dictionnary.
    # Returns the decrypted message or None if it is not possible.
    def brute_force(message, dict):
        message = message.upper()
        for a in range(26):
            if Affine.xgcd(a, 26)[0] == 1:
                for b in range(26):
                    decrypted_message = Affine.decrypt(a, b, message)
                    if dict.recognize(decrypted_message) > 0.7:
                        return decrypted_message
        return None

if __name__ == '__main__':
    Affine.brute_force()
