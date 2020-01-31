alphabet = ['a','b','c','d', 'e','f','g', 'h', 'i','j','k', 'l', 'm','n', 'o', 'p','q', 'r','s','t','u','v', 'w','x','y','z']
upalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#functions
def check(a):
    b = 0
    for i in range(2,len(alphabet)):
        if len(alphabet)%i==0 and a%i==0:
            b+=1
    return b is 0
def space_index(str):
    space = []
    for i in range(len(str)):
        if (str[i:i + 1] == " ") or (str[i:i + 2] == ", "):
            space.append(i)
    return(space)
def power(l):
    sub = []
    p=1
    for i in range(2,l):
        if l%i==0:
            l = l/i
            sub.append(i)
        if l==1:
            break
    for i in sub:
        p = p*i*(1-(1/i))
    return p
def key(k):
    p = power(len(alphabet))
    key = k**(p-1)%len(alphabet)
    return int(key)

#keys
while True:
    k1 = int(input("Enter first key number: "))
    k1 = k1 % len(alphabet)
    if check(k1):
        break

k2= int(input("Enter second key number: "))
k2= k2 % len(alphabet)



m = input("Enter your secret: ")
space =space_index(m)

#what to do?
ans = input("Do you want to encrypt? ")
if ans == "yes" or ans == "y":
#encryption
    c =[]
    for let in m:
        if let not in alphabet and let not in upalphabet:
            c.append(let)
            continue
        if let.islower():
            n = (alphabet.index(let)*k1+k2)%len(alphabet)
            c.append(alphabet[n])
            continue
        if let.isupper():
            n = (upalphabet.index(let)*k1+k2)%len(upalphabet)
            c.append(upalphabet[n])
            continue
        print("Cipher: "+"".join(c))
elif ans =="no" or ans=="n":
    ans = input("Do you want to decrypt? ")
    if ans =="yes" or ans =="y":
    #decription
#        decr = input("Do you want to decrypt? ")
        key = key(k1)
        decrypted = []
        c = m
#        if decr =="yes" or decr =="y":
        for let in c:
            if let.islower():
                n = (alphabet.index(let)-k2)*key%len(alphabet)
                decrypted.append(alphabet[n])
                continue
            if let.isupper():
                n = (upalphabet.index(let)-k2)*key%len(upalphabet)
                decrypted.append(upalphabet[n])
                continue
            if let not in alphabet and let not in upalphabet:
                decrypted.append(let)
                continue
            for index in space:
                decrypted.insert(index," ")
        print("Text: "+"".join(decrypted))
else:
    print("Thank you")
