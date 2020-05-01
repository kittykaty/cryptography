# GOST 28147
# Gamma mode with back network
from itertools import islice
import func_gost as f

def main():

    c1 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    c2 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

    # key
    key = input("Key: ")
    if len(key) < 32:
        key = f.repeat_to_length(key, 32) # make sure key has 32 char to make 256 bits

    bit_key = [] # list of 256b
    for letter in key:
        k = f.letter_to_binarylist(letter) # convert one char to 8 bits
        bit_key.append(k) # append bits to bit key

    keys = f.keys_from_key(bit_key)
    key_reversed = []
    for i in reversed(keys):
        key_reversed.append(i)


    # sync
    sync = input("Sync: ")
    if len(sync) < 8:
         sync = f.repeat_to_length(sync, 8)

    bit_sync = [] #
    for letter in sync:
        k = f.letter_to_binarylist(letter) # convert one char to 8 bits
        bit_sync += k

    # message
    message = input("Plain text: ")
    start_len = len(message)
    if start_len < 16:
        message = f.repeat_to_length(message, 16)  # make sure message has 16 char to make 128 bits

    mes_in_bits = [] # list of bits of letters in message
    for letter in message:
        m = f.letter_to_binarylist(letter)  # convert one char to 8 bits
        mes_in_bits.append(m)

    mes = f.mes_list(mes_in_bits)

    mes1 = mes[0:64]
    mes2 = mes[64:]


    mes_before = mes.copy()


    #first block of text
    n12 = bit_sync
    # gamma
    n12 = f.simple_change_encryption(n12, keys, key_reversed)
    # cipher
    n12_fin = f.add_mod_2(n12,mes1)

    # second block of text
    # n12 for second block is n1(32...1,2) n2(64...34,33)
    u12 = n12_fin[31:1:-1] + n12_fin[0:2] + n12_fin[64:33:-1] + n12_fin[33:31:-1]

    # gamma
    u12 = f.simple_change_encryption(u12, keys, key_reversed)
    # cipher
    u12_fin = f.add_mod_2(u12, mes2)



    #decryption
    d1 = f.add_mod_2(n12, n12_fin)
    d2 = f.add_mod_2(u12, u12_fin)

    result_of_encr = list(f.divide_chunks(n12_fin + u12_fin, 8))

    for i in range(len(result_of_encr)):
        result_of_encr[i] = f.binary_to_letter(result_of_encr[i])
    print("Encrypted message: {}".format("".join(result_of_encr)))


    result_of_decr = list(f.divide_chunks(d1 + d2, 8))

    for i in range(len(result_of_decr)):
        result_of_decr[i] = f.binary_to_letter(result_of_decr[i])
    print("Decrypted message: {}".format("".join(result_of_decr[0:start_len])))

    #print((d1+ d2) == mes_before)



main()
