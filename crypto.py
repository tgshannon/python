""" crypto.py
Take a plaintext message and encrypt it using a Ceasar cipher
"""

### Import libraries
import string

### Constants defined
CHAR_SET = string.printable[:-5]
SUBSTITUTION_CHARS = CHAR_SET[-3:]+CHAR_SET[:-3]
# generate encryption dictionary from substitution character set
ENCRYPTION_DICT = {}
for (i,k) in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHARS[i]
    ENCRYPTION_DICT[k] = v

TEST_MESSAGE = "I like Monty Python. They are very funny."

### Functions defined
def encrypt_msg(plaintext, encrypt_dict):
    """Take a plaintext message and encrypt each character using a
    Ceasar cipher (d->a). Return the cipher text."""
    ciphertext = []
    for k in plaintext:
        v = encrypt_dict[k]
        ciphertext.append(v)
        
    return ''.join(ciphertext)

### Testing code
ciphertext = encrypt_msg(TEST_MESSAGE, ENCRYPTION_DICT)
print(TEST_MESSAGE)
print(ciphertext)
