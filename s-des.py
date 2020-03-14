import func_file
from bitstring import BitArray
#KEY GENERTION

#key generation
key = int(input("Input key: "))
#k = map(int, [x for x in '{:0{size}b}'.format(key,size=10)])
k = [int(x) for x in '{:0{size}b}'.format(key,size = 10)]
print(k)
# 3 5 2 7 4 10 1 9 8 6
# p10
p10 = [k[2],k[4],k[1],k[6],k[3],k[9],k[0],k[8],k[7],k[5]]

#shift elements to left by 1 position
p1 = func_file.cycle_parts(p10[0:len(p10) // 2], 1) + func_file.cycle_parts(p10[len(p10) // 2: len(p10)], 1)

#replace elements for first key
k1 = func_file.key_replace(p1)

#shift elements to left by 2 positions
p2 = func_file.cycle_parts(p1[0:len(p1) // 2], 2) + func_file.cycle_parts(p1[len(p1) // 2:len(p1)], 2)

#repalce elements for second key
k2 = func_file.key_replace(p2)

#print 2 keys
print("Key 1: {}".format(k1))
print("Key 2: {}".format(k2))



#messsage
m = int(input("Input messsage: "))
m = [int(x) for x in '{:0{size}b}'.format(m,size = 8)]
print("Message in binary is: {}".format(m))

m = func_file.m_replace(m)


#first cycle
r = func_file.ext_4(m[4:len(m)])
print(r)

#result of F function
res1 = func_file.round(r, k1)



#final XOR unchanged left 4 bits of m and changed  right 4 bits of m
left = m[0: len(m)//2]
for i in range(len(left)):
    left[i] = (left[i] + int(res1[i])) % 2
#right part


#second_cycle
#final left part becomes right
l = func_file.ext_4(left)
res2 = func_file.round(l, k2)

right = m[4:len(m)]
for i in range(len(right)):
    right[i] = (right[i] + int(res2[i])) % 2



c = right + left
c = func_file.m_rereplace(c)
print("Encrypted: {}".format(c))
print("Encrypted integer is: {}".format(int("".join(str(x) for x in c), 2)))

print()
answer = input("Start decryption process? ")
if(answer == 'y'):
#decryption
    cipher = func_file.m_replace(c)
    print("Replaced cipher is: {}".format(cipher))
    #first cycle
    c1 = func_file.ext_4(cipher[4:len(cipher)])
    cres1 = func_file.round(c1, k2)
    cleft = cipher[0:len(cipher)//2]
    for i in range(len(cleft)):
        cleft[i] = (cleft[i] + int(cres1[i])) % 2

    cl = func_file.ext_4(cleft)
    cres2 = func_file.round(cl, k1)
    cright = cipher[4:len(cipher)]
    for i in range(len(cright)):
        cright[i] = (cright[i] + int(cres2[i])) % 2

    mes = func_file.m_rereplace(cright + cleft)
    print("Decrypted: {}".format(mes))
    print("Decrypted integer is: {}".format(int("".join(str(x) for x in mes), 2) ))
