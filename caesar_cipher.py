def encrypt():
    inp_msg = input("Enter secret message: ").upper()
    inp_spins = int(input("Enter number of letters to be shifted: "))
    
    split_msg = list(inp_msg)

    for l in split_msg:
        if (ord(l) == 32):
            print(l, end='')
        elif (ord(l) + inp_spins > 90):
            n = (ord(l) - 65 + inp_spins) % 26
            print(chr(n + 65), end='')
        else:
            print(chr(ord(l) + inp_spins), end='')
    print()

def decrypt():
    inp_msg = input("Input message to decrypt: ").upper()
    inp_spins = int(input("Enter number of letters to be shifted: "))

    split_msg = list(inp_msg)

    for l in split_msg:
        if (ord(l) == 32):
            print(l, end='')
        elif (ord(l) - inp_spins < 65):
            n = (ord(l) + 90 - inp_spins) % 26
            print(chr(65 + n), end='')
        else:
            print(chr(ord(l) - inp_spins), end='')
    print()
    
encrypt()
decrypt()