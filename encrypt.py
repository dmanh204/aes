from aes import *

plaintext = 0x0123456789abcdeffedcba9876543210
textblock = []
for i in range(16):
    a = 0xff << (15-i)*8
    a = a & plaintext
    a = a >> (15-i)*8
    textblock.append(a)

key = 0x0f1571c947d9e8590cb7add6af7f6798
keyblock = []
for i in range(16):
    a = 0xff << (15-i)*8
    a = a & key
    a = a >> (15-i)*8
    keyblock.append(a)

w =[]
keyexpansion(keyblock, w)

ketqua = encrypt(textblock, w)
for i in range(11):
    inketqua(ketqua[i])
print("Ciphertext: ")
inketqua(ngangdoc(ketqua[10]))