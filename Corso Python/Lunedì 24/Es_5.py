dizionario = {}

s = input("Inserire una stringa: ")

for i in range(len(s)):
    if s[i] in dizionario:
        dizionario[s[i]] += 1
    else:
        dizionario[s[i]] = 1


print(dizionario)            