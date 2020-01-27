alphabet = ['a','b','c','d', 'e','f','g', 'h', 'i','j','k', 'l', 'm','n', 'o', 'p','q', 'r','s','t','u','v', 'w','x','y','z']
upalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k = 3
text = input("Enter your secret: ")

def space_index(str):
    space = []
    for i in range(len(str)):
        if (str[i:i + 1] == " ") or (str[i:i + 2] == ", "):
            space.append(i)
    return(space)
space =space_index(text)

#encryption
ciphertext =[]
for letter in text:
    if letter not in alphabet and letter not in upalphabet:
        ciphertext.append(letter)
        continue
    if letter.islower():
        n = (alphabet.index(letter)+k)%len(alphabet)
        ciphertext.append(alphabet[n])
        continue
    if letter.isupper():
        n = (upalphabet.index(letter)+k)%len(upalphabet)
        ciphertext.append(upalphabet[n])
        continue
print("Cipher: "+"".join(ciphertext))

#decription
decr = input("Do you want to decrypt? ")
decrypted = []
if decr =="yes" or decr =="y":
    for letter in ciphertext:
        if letter.islower():
            n = (alphabet.index(letter)-k)%len(alphabet)
            decrypted.append(alphabet[n])
            continue
        if letter.isupper():
            n = (upalphabet.index(letter)-k)%len(upalphabet)
            decrypted.append(upalphabet[n])
            continue
    for index in space:
        decrypted.insert(index," ")
    print("Text: "+"".join(decrypted))
else:
    print("Thank you")
