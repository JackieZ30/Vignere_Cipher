from string import ascii_uppercase


def substitution_encrypt(cipher, plaintext):
    """Encrypt the plaintext using the given cipher."""
    ciphertext = ''
    for c in plaintext:
        try:
            ciphertext += cipher[c]
        except KeyError:
            pass
    return ciphertext

# Alternate solution
# =============================================================================
# def substitution_encrypt(cipher, plaintext):
#     """Encrypt the plaintext using the given cipher."""
#     return ''.join(cipher.get(c, '') for c in plaintext)
# =============================================================================


def decryption_cipher(encryption_cipher):
    """Given an encryption cipher, return its decryption cipher."""
    cipher = dict()
    for plaintext, ciphertext in encryption_cipher.items():
        cipher[ciphertext] = plaintext.upper()
    return cipher

# Alternate solution
# =============================================================================
# def decryption_cipher(encryption_cipher):
#     """Given an encryption cipher, return its decryption cipher."""
#     return {c : p.upper() for p, c in encryption_cipher.items()}
# =============================================================================



def caesar_shift_cipher(key):
    """Return a dictionary defining a Caesar shift cipher which encrypts 'A' 
    as <key>. The keys in the dictionary are plaintext characters, and the 
    values are ciphertext characters. Note that <key> can be an uppercase 
    or lowercase letter, but either way the ciphertext will be uppercase.
    """
    cipher = dict()
    i = ord(key.upper())
    for plaintext in ascii_uppercase:
        cipher[plaintext] = chr(i)
        cipher[plaintext.lower()] = chr(i)
        i += 1
        if i > ord('Z'):
            i = ord('A')
    return cipher

# Alternate solution
# =============================================================================
# def caesar_shift_cipher(key):
#     """Return a dictionary defining a Caesar shift cipher which encrypts 'A' 
#     as <key>. The keys in the dictionary are plaintext characters, and the 
#     values are ciphertext characters. Note that <key> can be an uppercase 
#     or lowercase letter, but either way the ciphertext will be uppercase.
#     """
#     i = ascii_uppercase.index(key.upper())
#     return keyword_cipher((ascii_uppercase * 2)[i:i+26])
# =============================================================================


def keyword_cipher(keyword):
    """Return the keyword cipher defined by the given keyword."""
    cipher = dict()
    for plaintext in ascii_uppercase:
        # Search for the character c that will encrypt the plaintext character
        # It's the first character in (keyword + ascii_uppercase) not used yet
        for c in keyword + ascii_uppercase:
            if c not in cipher.values():
                cipher[plaintext] = c
                cipher[plaintext.lower()] = c
                break
    return cipher


def vigenere_encrypt(keyword, plaintext):
    """Encrypt the plaintext, using a Vigenere cipher with the given keyword.
    Assumes that all characters in the keyword are letters.
    """
    ciphers = [caesar_shift_cipher(c) for c in keyword]
    ciphertext = ''
    i = 0
    for char in plaintext:
        cipher_char = substitution_encrypt(ciphers[i % len(ciphers)], char)
        if cipher_char: # Make sure we only increase i if char was a letter
            ciphertext += cipher_char
            i += 1
    return ciphertext


def vigenere_decrypt(keyword, ciphertext):
    """Decrypt the ciphertext, which was encrypted using a Vigenere cipher 
    with the given keyword. All characters in the keyword should be letters.
    """
    # Find the decryption keyword corresponding to the encryption keyword, by
    # reversing the alphabet shift for each character in the keyword.
    shifts = [ascii_uppercase.index(c) for c in keyword.upper()]
    decryption_keyword = ''.join(ascii_uppercase[-shift] for shift in shifts)
    
    return vigenere_encrypt(decryption_keyword, ciphertext)
