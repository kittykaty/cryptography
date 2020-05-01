
def letter_to_binarylist(letter):
    return [int(x) for x in "{:0{size}b}".format(ord(letter), size = 8)]

def binary_to_letter(bits):
    return chr(int("".join(str(y) for y in bits), 2))# convert list of bits to int, int to ASCII char

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def keys_from_key(key):
    key = [key[0] + key[1] + key[2] + key[3], key[4] + key[5] + key[6] + key[7], key[8] + key[9] + key[10] + key[11], key[12] + key[13] + key[14] + key[15],
    key[16] + key[17] + key[18] + key[19], key[20] + key[21] + key[22] + key[23], key[24] + key[25] + key[26] + key[27], key[28] + key[29] + key[30] + key[31]]
    return key

def mes_list(message):
    if len(message) == 16:
        return message[0] + message[1] + message[2] + message[3] + message[4] + message[5] + message[6] + message[7] + message[8] + message[9] + message[10] + message[11] + message[12] + message[13] + message[14] + message[15]
    return message[0] + message[1] + message[2] + message[3] + message[4] + message[5] + message[6] + message[7]

def left_from_64(message):
        return message[0:32]
def right_from_64(message):
        return message[32:]

def binary_to_decimal(binary_list):
    return int("".join(str(x) for x in binary_list), 2)

def left_plus_key(left, key):
    left = binary_to_decimal(left)
    key = binary_to_decimal(key)
    res_in_dec = (left + key) % 4294967296 # mod(2^32)
    return [int(x) for x in "{:0{size}b}".format(res_in_dec, size = 32)]

def mod_2_32(one, two):
    return left_plus_key(one, two)

def mod_2_32_1(one, two):
    one = binary_to_decimal(one)
    two = binary_to_decimal(two)
    res_in_dec = (one + two) % 4294967295
    return [int(x) for x in "{:0{size}b}".format(res_in_dec, size = 32)]

def s_block(bits):

    #list of 8 lists of 4 bits = 32 bits
    bits = list(divide_chunks(bits, 4))
# s-block:
# number |         value
#         | 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
#         |________________________________________________
#    0    | 04 10 09 02 13 08 00 14 06 11 01 12 07 15 05 03
#    1    | 14 11 04 12 06 13 15 10 02 03 08 01 00 07 05 09
#    2    | 05 08 01 12 10 03 04 02 14 15 12 07 06 00 09 11
#    3    | 07 13 10 01 00 08 09 15 14 04 06 12 11 02 05 03
#    4    | 06 12 07 01 05 15 13 08 04 10 09 14 00 03 11 02
#    5    | 04 11 10 00 07 02 01 13 03 06 08 05 09 12 15 14
#    6    | 13 11 04 01 03 15 05 09 00 10 14 07 06 08 02 12
#    7    | 04 10 09 02 13 08 00 14 06 11 01 12 07 15 05 03

    s = [ [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
          [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
          [5, 8, 1, 12, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
          [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
          [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
          [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
          [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
          [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3]
          ]

    ints = [] # list of 8 decimal changed numbers
    count = 0
    for bit in bits:
        b = binary_to_decimal(bit)
        b_1 = s[count][b]
        ints.append(b_1)
        count += 1

    res = []
    for i in ints:
        res.append([int(x) for x in "{:0{size}b}".format(i, size = 4)])

    res = res[0]+ res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]
    return res

def cycle_parts(l, ti):
    if (ti == 1):
        tmp = l[0]
        l.pop(0)
        l.append(tmp)
        return l
    return cycle_parts(cycle_parts(l, 1), ti - 1)

def move_11(list_of_bits):
    list_of_bits = cycle_parts(list_of_bits, 11)
    return list_of_bits

def add_mod_2(left, right):
    res = []
    for i in range(len(left)):
        res.append((left[i] + right[i]) % 2)
    return res


def encryption(mes_in_bits, key):
    left_start = left_from_64(mes_in_bits) # 32 bits
    right_strat = right_from_64(mes_in_bits) # 32 bits

    # func with key
    left_1 = left_plus_key(left_start, key)
    #print("Letf + key: ")
    #print(left_1)

    # s-change
    left_1 = s_block(left_1)
    #print("Letf + s-block: ")
    #print(left_1)

    # move 11 positions to the left
    left_1 = move_11(left_1)
    #print("move_11: ")
    #print(left_1)

    #print(left_1)

    # add left and right part mod 2
    left_1 = add_mod_2(left_1, right_strat)
    #print("left + right: ")
    #print(left_1)

    left_fin = left_1
    right_fin = left_start

    result_of_encr = left_fin + right_fin
    return result_of_encr


def simple_change_encryption(n, keys, key_reversed):
    #simple change encryption
    for i in range(3):
        for key in keys:
            n_e = encryption(n, key)
            n = n_e


    for key in key_reversed:
        n_e = encryption(n, key)
        n = n_e

    n = n[32:] + n[0:32]

    return n
