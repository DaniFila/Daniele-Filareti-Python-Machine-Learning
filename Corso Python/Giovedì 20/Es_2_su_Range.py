# PUNTO 1
N = int(input("inserire un numero (verifico se pari o dispari): "))   # si richiede il numero

if N%2 == 0:  # si verifica il resto della divisione per 2, se 0 allora è pari, dispari altrimenti
    print("Pari")
else:
    print("Dispari")

#--------------------------------------------------------------------------
# PUNTO 2

n = int(input("inserire un numero (stampo numeri da n a 0): "))   # richiesta numero
if n>=0:   #verifica se numero è maggiore o uguale a 0
     for i in range(n,-1,-1):    # scan dal numero fino a 0
         print(i)
else:
    print("numero negativo")       # se negativo  
a = int(input("Vuoi continuare? (1/0): "))      #mess per ripetere operazione   
while a == 1:
    n = int(input("inserire un numero: "))
    if n>=0:                          # ciclo che ripete fino a variabile a == 0
        for i in range(n,-1,-1):
               print(i)
    else:
        print("il numero è negativo")
    a = int(input("Vuoi continuare? (1/0): "))    

#-----------------------------------------------------------------------
# PUNTO 3

L = [] # lista per inserire numeri da input
L2 = [] # lista contenente tutti i numeri presi in input al quadrato
k = int(input("inserire un numero (-1 per terminare): "))  
if k != -1:
    L.append(k)          # Ciclo con numeri presi in input e inseriti in L fin quando k == -1
    while k != -1:
        k = int(input("inserire un numero (-1 per terminare): "))
        if k != -1:
            L.append(k)



for i in range(len(L)):   # scorrimento della lista L e per ogni numero si fa il quadrato e si aggiunge in L2
    L2.append(L[i]*L[i])

print("LISTA INIZIALE")
print(L)
          # Stampe finali delle 2 liste
print("")

print("LISTA FINALE")
print(L2)


