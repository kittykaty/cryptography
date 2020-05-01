#GOST 28147
#simple change
from itertools import islice
import func_gost as f

def main():

    key = input("Key: ")
    if len(key) < 32:
        key = f.repeat_to_length(key, 32) # make sure key has 32 char to make 256 bits

    bit_key = [] # list of 256b
    for letter in key:
        k = f.letter_to_binarylist(letter) # convert one char to 8 bits
        bit_key.append(k) # append bits to bit key

    keys = f.keys_from_key(bit_key) # list of 8 keys length of each = 32


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


    #encryption

    key_reversed = []
    for i in reversed(keys):
        key_reversed.append(i)

    #encryption
    round = 0
    for i in range(3):
        for key in keys:
            c = f.encryption(mes, key)
            mes = c
            round +=1

    for key in key_reversed:
        c = f.encryption(mes, key)
        mes = c
        round += 1

    mes = mes[32:] + mes[0:32]

    result_of_encr = list(f.divide_chunks(mes, 8))

    for i in range(len(result_of_encr)):
        result_of_encr[i] = f.binary_to_letter(result_of_encr[i])
    print("Encrypted message: {}".format("".join(result_of_encr)))


    #decryption
    for key in keys:
        c = f.encryption(mes, key)
        mes = c
        round += 1

    for i in range(3):
        for key in key_reversed:
            c = f.encryption(mes, key)
            mes = c
            round +=1

    mes = mes[32:] + mes[0:32]

    result_of_decr = list(f.divide_chunks(mes, 8))

    for i in range(len(result_of_decr)):
        result_of_decr[i] = f.binary_to_letter(result_of_decr[i])
    print("Decrypted message: {}".format("".join(result_of_decr[0:start_len])))

    #print(mes_before == mes)

main()
