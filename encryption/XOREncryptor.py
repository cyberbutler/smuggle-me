from itertools import cycle
def encrypt(plaintext, key, *args, **kwargs):
    if len(plaintext) > len(key):
        repeatingKey = ''.join(map(lambda p, k: k, plaintext, cycle(key))).encode('utf-8')
        zippedBytes = zip(*map(bytearray, [plaintext, repeatingKey]))
    else:
        zippedBytes = zip(*map(bytearray, [plaintext, key.encode('utf-8')]))
        
    ciphertext = bytearray(a^b for a, b in zippedBytes)
    return ciphertext