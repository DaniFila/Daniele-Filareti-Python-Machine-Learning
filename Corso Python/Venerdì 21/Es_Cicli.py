# PUNTO 1

somma = 0  # variabile per aggiungere somma interi

n = int(input("inserire numeri interi, 0 per chiudere: "))  # n da input
if n !=0:  # se diverso da 0 si somma alla variabile
    somma+=n
while n != 0:   # finché diverso da 0 si ripete 
    n = int(input("inserire numeri interi, 0 per chiudere: "))
    if n!=0:
        somma+=n


print("La somma dei numeri è:", somma)        # stampa del risultato.

#---------------------------------------------

# PUNTO 2

stringa = input("Inserire una stringa: ")   # stringa da input

for i in range(len(stringa)):  # scan della stringa con il len della string
    print(stringa[i])  # stampa di ciascun carattere


#----------------------------------------------

# PUNTO 3

N = int(input("Indicare massimo numero range: "))
S = int(input("indicare lo step per il range: "))

for i in range(0,N,S):
    print(i)