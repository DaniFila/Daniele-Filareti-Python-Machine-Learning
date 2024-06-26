with open("Mercoledi 26\Es2.txt","r") as file:
    stringa=file.read()

print("Il contenuto del file è:",stringa)
righe = stringa.split("\n")
#print(righe)
print("\n\nIl numero di righe è: ",len(righe))       #numero righe

punteggiatura="!.,;: "

sum=0
for parola in righe:
    sum+=len(parola)
print("somma caratteri è: ",sum)
lista_parole=[]

conta_par=0
for riga in righe:
    lista_parole=riga.split(" ")
    #print(lista_parole)
    conta_par+=len(lista_parole)

print("Numero parole: ", conta_par)
