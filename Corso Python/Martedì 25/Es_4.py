l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

stringa = input("inserire la stringa: ")
key = int(input("indicare chiave di cifratura: "))
crypt = ""
for i in range(len(stringa)):
    a = (l.index(stringa[i]) +key) % 25
    crypt+=l[a]

print(crypt)



