def HexToBinary(hex):
    return bin(int(hex, 16))[2:].zfill(len(list(hex))*4)


def BinaryToHex(binary):
    return hex(int(binary, 2)).split('x')[-1].upper()
