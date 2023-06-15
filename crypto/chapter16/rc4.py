def KSA(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    S = S[:]
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key = S[(S[i] + S[j]) % 256]
        yield key

def xor(a, b):
    return a ^ b

plaintext = b'helloworld'
S = KSA(b'testkey')
ciphertext = bytes(map(xor, plaintext, PRGA(S)))
print(ciphertext)
plaintext = bytes(map(xor, ciphertext, PRGA(S)))
print(plaintext)