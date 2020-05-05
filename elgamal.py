#Elgamal
import random

def main():

    # choose p and count q
    while True:
        p = int(input("Choose prime number p: "))
        q = (p - 1) // 2

        if isprime(p) and isprime(q):
            break
        print("You should choose prime number")

    #choose g
    while True:
        g = int(input("Choose number g: "))

        if 1 < g < (p - 1) and (g**q) % p != 1:
            break
        print("You should choose another number (bigger than 1 and less than {})".format(p - 1))

    # abonent A choose secret key
    while True:
        da = int(input("Abonent A's secret number is: "))
        if 1 < da < (p - 1):
            break
        print("You should choose another number (bigger than 1 and less than {})".format(p - 1))

    # abonent B choose secret key
    while True:
        db = int(input("Abonent B's secret number is: "))
        if 1 < db < (p - 1):
            break
        print("You should choose another number (bigger than 1 and less than {})".format(p - 1))

    # calculation of ea eb (public keys)
    ea = publickey(g, da, p)
    eb = publickey(g, db, p)

    # generate k
    k = random.randint(2, p - 2)

    #message
    while True:
        m = int(input("Message: "))
        if m < p:
            break

    while True:
        sender = input("Choose the sender: ")
        if sender == "A":
            e = eb
            d = db
            break
        elif sender == "B":
            e = ea
            d = da
            break
        else:
            print("You should choose A/B")

    #calculate r and c
    r = (g**k) % p
    c = (m * e**k) % p

    print("Sent: c = {}, r = {}".format(c,r))

    #decryption
    m2 = (c * (r**(p-1-d))) % p

    #print(m2 == m)
    print("Recieved message: {}".format(m2))

# functions
def isprime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
    return True

def publickey(g, d, p):
    return (g**d) % p


main()
