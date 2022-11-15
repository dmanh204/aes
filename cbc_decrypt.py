from aes import *
with open("cbc_key.txt", "r") as k:

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

with open("cbc_initial.txt", "r") as initial:
    initial_value = int(initial.read(), 16)
    initial_block = []
    for i in range(16):
        a = 0xff << (15-i)*8
        a = a & initial_value
        a = a >> (15-i)*8
        initial_block.append(a)

with open("cbc_ciphertext.txt", "r", encoding="UTF-8") as text, open("cbc_decrypted.txt", "w", encoding="UTF-8") as kq:
    a = 0
    block = []
    sub_block = initial_block.copy()
    while True:
        byte = text.read(1) # Doc 1 byte
        if byte == "":      # Neu doc duoc EOF thi break
            break
        byte = ord(byte)    # chuyen gia tri char -> int
        block.append(byte)
        a += 1              # Tang a len 1
        if a == 16:
            temp = decrypt(block, w)
            ketqua = ngangdoc(temp[10])
            for i in range(16):
                ketqua[i] = ketqua[i] ^ sub_block[i]
            for i in range(16):
                kq.write(chr(ketqua[i]))

            sub_block = block.copy()
            block.clear()
            a = 0

    