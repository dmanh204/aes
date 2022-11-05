from aes import *

ciphertext = 0xff0b844a0853bf7c6934ab4364148fb9

textblock = []
for i in range(16):
    a = 0xff << (15-i)*8
    a = a & ciphertext
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

ketqua = decrypt(textblock, w)

for i in range(11):
    inketqua(ketqua[i])
print("Plaintext: ")
inketqua(ngangdoc(ketqua[10]))
