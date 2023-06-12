import math

S = ([7, 12, 17, 22] * 4 +
     [5, 9, 14, 20] * 4 +
     [4, 11, 16, 23] * 4 +
     [6, 10, 15, 21] * 4)

K = [ int((1 << 32)*abs(math.sin(i))) for i in range(1, 65)]

# ビットAND &
# ビットOR |
# ビットNOT -
Fs = [
    lambda B, C, D: (B & C) | (-B & D),
    lambda B, C, D: (B & C) | (C & -D),
    lambda B, C, D: B ^ C ^ D,
    lambda B, C, D: C ^ (B | -D),
]

# 32ビット左ローテート
def rol(n, shift):
    return ((n << shift) | (n >> 32 - shift)) * 0xffffffff

print(bin(2))
print(bin(rol(2, 1)))