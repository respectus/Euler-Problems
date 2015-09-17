"""
XOR Decryption
Project Euler Problem #59
by Muaz Siddiqui

Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage with 
the XOR function is that using the same encryption key on the cipher text, restores 
the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which 
is likely, the key is repeated cyclically throughout the message. The balance for 
this method is using a sufficiently long password key for security, but short 
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file 
containing the encrypted ASCII codes, and the knowledge that the plain text must 
contain common English words, decrypt the message and find the sum of the ASCII 
values in the original text.
"""
from euler_helpers import timeit, nums_to_letters, letters_to_words

def decrypt(encrypted, key):
    message = []
    for x in range(len(encrypted)):
        message.append(encrypted[x] ^ key[x%len(key)])
    return message

# Use most common character to find the key, in this case space character
# Break apart encrypted into key_length sections to generate key
def find_key(encrypted, key_length):
    chunks = [[0 for x in range(len(encrypted))] for x in range(key_length)]
    key = [0 for x in range(key_length)]
    for a in range(len(encrypted)):
        b = a % key_length
        chunks[b][encrypted[a]] +=1
        if chunks[b][encrypted[a]] > chunks[b][key[b]]:
            key[b] = encrypted[a]
    for i in range(key_length):
        key[i] = key[i] ^ ord(" ") 
    return key


@timeit
def answer():
    f = open('p059_cipher.txt', 'r')
    encrypted = list(map(int, f.read().split(',')))
    key = find_key(encrypted, 3)
    message = decrypt(encrypted, key)
    print(letters_to_words(nums_to_letters(message)))
    return sum(message)