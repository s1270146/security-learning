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
    return ((n << shift) | (n >> 32 - shift)) & 0xffffffff

# ブロックサイズになるようにパディング
def md5_pad(msg, offset=0):
    
    # メッセージの長さにオフセット値を加えた値をmsg_lenに格納
    msg_len = len(msg) + offset

    # メッセージに`b'\x80'` を追加、パディングの開始を示す
    msg += b'\x80'

    # メッセージの長さとオフセット値の合計を64で割ったあまりが56より大きいかそうでないかで分ける
    # 大きい場合
    if (len(msg) + offset) % 64 > 56:
        msg += b'\x00' * ((64 - (len(msg) + offset) % 64) + 56)
    # 小さい場合
    else:
        msg += b'\x00' * (56 - (len(msg) + offset) % 64)

    # msg_len << 3 では、3ビット左にしている、すなわち8倍している
    # to_bytes(8, byteorder='little')は、整数をリトルエンディアンのバイト列に変換するメソッド
    msg += (msg_len << 3).to_bytes(8, byteorder='little')
    return msg

def md5(msg, IV=(0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476), offset=0):
    A0, B0, C0, D0 = IV
    msg = md5_pad(msg, offset)

    gs = [(1, 0), (5, 1), (3, 5), (7, 0),]
    for i in range(len(msg) // 64):
        block = msg[i*64:(i+1)*64]
