import hashlib
import sys
import random
from binascii import hexlify, unhexlify

SALT = b'secretsalt'

print('Register')
username = input('user name > ').encode()
if b'=' in username:
    print('Bye.')
    sys.exit(1)

# ユーザの名前と他の文字列を加えてバイトに変換する
userdata = b'priv=guest,username=' + username
h = hashlib.md5(SALT + userdata).hexdigest()
print('Your username(hex) is ', hexlify(username).decode())
print('Your signature is: ', h)
