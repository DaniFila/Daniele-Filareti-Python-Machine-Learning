stringa=input("Inserire una parola: ")
punteggiatura="!,.;-"
for let in punteggiatura:
    stringa=stringa.replace(let,"")

lista=list(stringa.lower().split(" "))

dizionario = {}
contr = False
for parola in lista:
    if lista.count(parola) >1:
        dizionario[parola] = lista.count(parola)
        contr = True


if contr:
    print("Le ripetizioni che abbiamo nella frase sono:",dizionario)
else:
    print("non c'è alcuna ripetizione.")    