import hashlib
import sys
import random
from binascii import hexlify, unhexlify

SALT = b'secretsalt'

#  ----- Register ----
print('Register')

# encode は utf-8に変換している
username = input('user name > ').encode()
if b'=' in username:
    print('Bye.')
    sys.exit(1)

# ユーザの名前と他の文字列を加えてバイトに変換する
userdata = b'priv=guest,username=' + username

# SALTとuserdataをmdを使って暗号化
# hexdigest()で16進形式文字列にする
h = hashlib.md5(SALT + userdata).hexdigest()

# hexlify は、 バイナリdataの16進表現
# ソルトとくっつけたuserdataを表示させている
print('Your userdata(hex) is ', hexlify(userdata).decode())
print('Your signature is: ', h)

# ---- Login ----
print('Login')

# unhexlifyで16進数表記を文字列に戻す
userdata = unhexlify(input('userdata(hex) > '))
sig = input('signature(hex) > ')

h = hashlib.md5(SALT + userdata).hexdigest()
if h == sig:
    print('Login OK!')

    if b'priv=admin' in userdata.split(b','):
        print('Congratulations! You are admin!')
    else:
        print('Sorry, admin only')

else:
    print('Bye.')
    sys.exit(1)
