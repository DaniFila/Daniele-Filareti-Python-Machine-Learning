""""
Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, quanti sono, quali sono e
quanto sono lunghi i duplicati.
Esempio:
‘La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde
e fiorito.’
#outpout
"La" appare 2 volte, lunghezza 2.
"""

stringa=input("Inserire una stringa: ")
punteggiatura="!,.;-"
for let in punteggiatura:
    stringa=stringa.replace(let,"")

lista=list(stringa.lower().split(" "))

#print(lista)
par=[]
rip=[]
contr=False
for parola in lista:
    count=lista.count(parola)
    if count>1 and parola not in par:
            par.append(parola)
            rip.append(count)
            contr=True

#print(rip)
if contr:
    for i in par:
        print(f"La parola {i} è ripetuta {rip[par.index(i)]} volte, di lunghezza {len(i)}")
else:
    print("Non c'è alcuna ripetizione")

#--------------------------------------
# con dizionario

stringa=input("Inserire una parola: ")
punteggiatura="!,.;-"
for let in punteggiatura:
    stringa=stringa.replace(let,"")

lista=list(stringa.lower().split(" "))

dizionario = {}
contr = False
for parola in lista:
    if lista.count(parola) >1:
        dizionario[parola] = {}
        dizionario[parola]["count"] = lista.count(parola)
        dizionario[parola]["lunghezza"] = len(parola)
        contr = True


if contr:
    print("Le ripetizioni che abbiamo nella frase sono:",dizionario)
else:
    print("non c'è alcuna ripetizione.")    