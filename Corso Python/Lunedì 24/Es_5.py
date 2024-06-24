dizionario = {}

s = input("Inserire una stringa: ")

for i in s:
    if i in dizionario:
        dizionario[i] += 1
    else:
        dizionario[i] = 1


print(dizionario)
