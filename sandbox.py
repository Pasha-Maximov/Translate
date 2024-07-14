pt = ""
ct = "zayhdilyyf"

for I in range(26):
    shift = I
    pt = ""
    for letter in ct:
        letter = chr((ord(letter) - 97 - (shift)) % 26 + 97)
        pt += letter
    print(pt)


