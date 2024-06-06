pt = ""
ct = "Zayhdilyyf"

for I in range(27):
    shift = I
    pt = ""
    for letter in pt:
        letter = chr(ord(letter) - (shift))
        pt += letter
    print(pt)


