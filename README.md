# Vigenère Cipher

This Python project implements various techniques to crack Vigenère ciphers, historically considered unbreakable due to their polyalphabetic nature. By leveraging cryptanalysis methods such as index of coincidence and frequency analysis, the program automates the process of decrypting ciphertexts encrypted with the Vigenère cipher.

## Files

1. **vigenere.py**: Contains functions for analyzing and decrypting Vigenère ciphertexts.
2. **ciphers.py**: Defines several substitution ciphers, including Caesar shift and keyword ciphers.
3. **vigenere_testing.py**: Demonstrates the functionality of the Vigenère cipher through tests on sample ciphertexts.

## Features

- **Index of Coincidence Calculation**: Determines the probability that two letters at a given distance in the ciphertext are the same, aiding in key length guessing.
- **Key Length Guessing**: Utilizes the index of coincidence to guess the length of the encryption key.
- **Frequency Analysis**: Performs frequency analysis on the ciphertext to guess individual Caesar shift keys used in the Vigenère cipher.
- **Vigenère Key Guessing**: Infers the complete encryption key by conducting frequency analysis for each position in the key.

## Usage

1. Ensure Python 3 is installed on your system.
2. Run the `test.py` script to execute tests on sample ciphertexts and verify the functionality of the Vigenère cipher cracker.

## Example

To decrypt a ciphertext file, use the `decrypt_file(filename)` function in `vigenere.py`. Replace `filename` with the name of the ciphertext file (without the `.txt` extension). The function will return the decryption key used and create a decrypted file with the suffix `-decrypted.txt`.

```python
import vigenere

# Decrypt a ciphertext file
decryption_key = vigenere.decrypt_file('example_ciphertext')
print("Decryption key:", decryption_key)
```

## Contribution
Contributions to this project are welcome! Feel free to submit issues or pull requests to suggest improvements or report bugs.
