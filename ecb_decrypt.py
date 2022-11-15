from aes import *
with open("ecb_key.txt", "r") as k:

    key = int(k.read(), 16)         # Doc key tu file
    keyblock = []
    for i in range(16):
        a = 0xff << (15-i)*8        # Lan luot dua a den lay 8 bit cua key
        a = a & key
        a = a >> (15-i)*8
        keyblock.append(a)               # Dua 8 bit lay duoc vao list
# Tao 11 key round
w =[]
keyexpansion(keyblock, w)

with open("ecb_ciphertext.txt", "r", encoding = "UTF-8") as text, open("ecb_decrypted.txt", "w", encoding ="UTF-8") as kq:
    a = 0
    block = []

    while True:
        byte = text.read(1)     # Doc 1 ky tu a.k.a 1 byte
        if byte == "":             # Neu byte == EOF thi break
            break
        byte = ord(byte)        # Chuyen dang char --> int
        block.append(byte)      # them byte vao block
        a += 1                  # a tang len 1
        if a == 16:
            temp = decrypt(block, w)  # Giai ma khoi AES
            ketqua = ngangdoc(temp[10])     # Trong mo ta AES, return cua ham decrypt la mot bo 11 list plaintext qua cac round
                                            # Nen ta lay list thu 11 la ket qua encrypt cuoi cung
            for i in range(16):
                kq.write(chr(ketqua[i]))

            block.clear()
            a = 0