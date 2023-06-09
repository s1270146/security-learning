from hashlib import sha1

BLOCK_SIZE = 64
ipad = b'\x36' * BLOCK_SIZE
opad = b'\x5c' * BLOCK_SIZE

def xor(s1: bytes, s2: bytes):
    return bytes([ a ^ b for a, b in zip(s1, s2)])
    # s1とs2で対応するバイトに対して^を使ってxor演算を行っている

def hmac_sha1(key: bytes, msg: bytes):
    if len(key) > BLOCK_SIZE:
        key = sha1(key).digest()

    key = key + b'\x00' * (BLOCK_SIZE - len(key))

    k_opad = xor(key, opad)
    k_ipad = xor(key, ipad)

    return sha1(k_opad + sha1(k_ipad + msg).digest())

secretkey = input('secretkey <- ')
somedata = input('somedata <- ')

print(hmac_sha1(secretkey.encode(), somedata.encode()).digest())

print(hmac_sha1(secretkey.encode(), somedata.encode()).hexdigest())

# digest()はbytes型に変換
# hexdigest()は16進数に変換