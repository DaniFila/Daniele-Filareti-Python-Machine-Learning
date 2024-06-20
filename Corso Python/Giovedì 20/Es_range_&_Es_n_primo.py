n = int(input("inserire un numero: "))   # richiesta numero
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


#---------------------------------------------------------#
print("ESERCIZIO 2")
print("")

count = 0   # contatore per numeri primi

N = int(input("inserire un numero: "))   # si richiede il numero
if N%2 != 0:  # si verifica il resto della divisione per 2, se 0 allora non è primo
    print("Il numero è primo")
    count+=1
else:
    print("il numero non è primo")

while count<5:   # si entra nel ciclo fin quando non si trovano 5 numeri primi
    N = int(input("inserire un numero: "))
    if N%2 != 0:
        print("Il numero è primo")
        count+=1
    else:
        print("il numero non è primo")    