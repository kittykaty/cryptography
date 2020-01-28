upalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet = ['a','b','c','d', 'e','f','g', 'h', 'i','j','k', 'l', 'm','n', 'o', 'p','q', 'r','s','t','u','v', 'w','x','y','z']
k = input("Enter your key-word: ")
m = input("Enter your secret: ")
c = [] #ciphertext

#devide words in text by spaces
def space_index(str):
    space = []
    for i in range(len(str)):
        if (str[i:i + 1] == " ") or (str[i:i + 2] == ", "):
            space.append(i)
    return(space)
space =space_index(m)

#encryption
for i in range(len(m)):
#make a circle around key phrase:
    ik =i
    if ik > (len(k)-1):
        ik=i%len(k)
#just add all non-alphabet characters to ciphertext
    if m[i] not in alphabet and m[i] not in upalphabet:
        c.append(m[i])
        continue
#change and add letters
    if m[i].isupper():
        n = (upalphabet.index(m[i])+alphabet.index(k[ik]))%len(upalphabet)
        c.append(upalphabet[n])
        continue
    if m[i].islower():
        n = (alphabet.index(m[i])+alphabet.index(k[ik]))%len(alphabet)
        c.append(alphabet[n])
        continue
print("Cipher: "+"".join(c))

#decription
decr = input("Do you want to decrypt? ")
decrypted = []
if decr =="yes" or decr =="y":
    for i in range(len(c)):
#make a circle around key phrase:
        ik =i
        if ik > (len(k)-1):
            ik=i%len(k)
        if c[i].isupper():
            n = (upalphabet.index(c[i])-alphabet.index(k[ik])+len(alphabet))%len(upalphabet)
            decrypted.append(upalphabet[n])
            continue
        if c[i].islower():
            n = (alphabet.index(c[i])-alphabet.index(k[ik])+len(alphabet))%len(alphabet)
            decrypted.append(alphabet[n])
            continue
#divide words
    for index in space:
        decrypted.insert(index," ")
    print("Text: "+"".join(decrypted))
else:
    print("Thank you")
