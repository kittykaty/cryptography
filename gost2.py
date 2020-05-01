#GOST 28147
#Gamma mode
from itertools import islice
import func_gost as f

def main():
    #constant
    c1 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    c2 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

    #key
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


    #sync
    sync = input("Sync: ")
    if len(sync) < 8:
         sync = f.repeat_to_length(sync, 8)

    bit_sync = [] #
    for letter in sync:
        k = f.letter_to_binarylist(letter) # convert one char to 8 bits
        bit_sync += k

    #message
    message = input("Plain text: ")
    start_len = len(message)
    if start_len < 8:
        message = f.repeat_to_length(message, 8)  # make sure message has 8 char to make 64 bits

    mes_in_bits = [] # list of bits of letters in message
    for letter in message:
        m = f.letter_to_binarylist(letter)  # convert one char to 8 bits
        mes_in_bits.append(m)
    mes = f.mes_list(mes_in_bits)
    mes_before = mes.copy()

    n1 = bit_sync[31::-1]
    n2 = bit_sync[64:31:-1]

    n12 = n1 + n2

    #simple change encryption 1
    n12 = f.simple_change_encryption(n12, keys, key_reversed)


    #n3 and n4 == n1 and n2
    n3 = n12[0:32]
    n4 = n12[32:]

    #changes with n3 and n4 blocks => 32 bits each
    n4 = f.mod_2_32_1(n4,c1)
    n3 = f.mod_2_32(n3,c2)

    n1 = n3
    n2 = n4

    n12 = n1 + n2
    #simple change encryption 2
    n12 = f.simple_change_encryption(n12, keys, key_reversed)

    #cipher = n12_fin, n12 = gamma
    n12_fin = f.add_mod_2(n12, mes)

    result_of_encr = list(f.divide_chunks(n12_fin, 8))

    for i in range(len(result_of_encr)):
        result_of_encr[i] = f.binary_to_letter(result_of_encr[i])
    print("Encrypted message: {}".format("".join(result_of_encr)))


    #decryption
    d = f.add_mod_2(n12, n12_fin)

    result_of_decr = list(f.divide_chunks(d, 8))

    for i in range(len(result_of_decr)):
        result_of_decr[i] = f.binary_to_letter(result_of_decr[i])
    print("Decrypted message: {}".format("".join(result_of_decr[0:start_len])))

    #print(d==mes_before)






main()
