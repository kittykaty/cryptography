#LFSR
key = int(input("Key: ")) # number to make start key
regist = [int(x) for x in '{:0{size}b}'.format(key,size = 11)]
def main():
    inp = input("Name of message file: ")
    out = input("Name of cipher file: ")

    first = open(inp, "r", encoding='utf-8')
    second = open(out, "w", encoding='utf-8')

    for line in first: # read lines of file
        for letter in line: # read letters of lines
            a = [int(x) for x in "{:0{size}b}".format(ord(letter), size = 8)] # convert letter to ASCII, convert int to list of bits
            c = []
            for bit in a: # for bit in bits
                x = change() #change bit of regist
                y = (bit + x) % 2 # XOR with regist bit
                c.append(y) # append changed bit to c array
            cipher = int("".join(str(y) for y in c), 2) # convert list of bits to int, int to ASCII char
            second.write(chr(cipher))

# (11, 2, 0)
def change():
    regist.pop(-1)
    x = (regist[2] + regist[0]) % 2
    regist.insert(0, x)
    return regist[-1]
main()
