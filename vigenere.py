
import ciphers
from collections import Counter
import string

# Frequency of each letter in standard English text. Taken from:
# https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
FREQUENCIES = {'A': 0.08167,
               'B': 0.01492,
               'C': 0.02782,
               'D': 0.04253,
               'E': 0.12702,
               'F': 0.02228,
               'G': 0.02015,
               'H': 0.06094,
               'I': 0.06966,
               'J': 0.00153,
               'K': 0.00772,
               'L': 0.04025,
               'M': 0.02406,
               'N': 0.06749,
               'O': 0.07507,
               'P': 0.01929,
               'Q': 0.00095,
               'R': 0.05987,
               'S': 0.06327,
               'T': 0.09056,
               'U': 0.02758,
               'V': 0.00978,
               'W': 0.02360,
               'X': 0.00150,
               'Y': 0.01974,
               'Z': 0.00074 }


def index_of_coincidence(txt, n):
    length = len(txt)
    count = 0
    total = 0
    for i in range(length - n):
        total += 1
        if txt[i] == txt[i + n]:
            count += 1
    
    if total == 0:
        return 0
    
    ic = count / total
    
    return ic

def guess_key_length(txt):
    length = len(txt)
    for n in range(1, length):
        if index_of_coincidence(txt, n) > 0.06:
            return n
    return 1

def guess_caesar_key(txt):
    ltr = ''
    best_score = 0
    for possible_key in string.ascii_uppercase:
        decrypted_txt = ''
        for i, char in enumerate(txt):
            decrypted_txt += chr((ord(char) - ord(possible_key) + 26) % 26 + ord('A'))
        score = 0
        d = Counter(decrypted_txt)
        for letter in string.ascii_uppercase:
            prob = d[letter] / len(decrypted_txt)
            score += prob * FREQUENCIES[letter]
        
        if score > best_score:
            best_score = score
            ltr = possible_key
    
    return ltr

def guess_vigenere_key(txt):
    n = guess_key_length(txt)
    key = ''
    for i in range(n):
        s = txt[i::n]
        key += guess_caesar_key(s)
    return key

def decrypt_file(filename):
    filename_renamed = filename + ".txt"
    with open(filename_renamed, 'r') as f:
        s = f.read()
    
    key = guess_vigenere_key(s)
    decrypted_txt = ciphers.vigenere_decrypt(key, s)
    
    decrypted_name = filename + "-decrypted.txt"
    with open(decrypted_name, 'w') as f:
        f.write(decrypted_txt)
        
    return key


