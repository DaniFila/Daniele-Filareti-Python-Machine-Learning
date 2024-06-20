# PUNTO 4

L = [] # lista per inserire numeri da input
k = input("inserire un numero (-1 per terminare): ")
if not k.isdigit():    # verifico che non si abbia digitato una lettera ma solo numeri interi
    print("errore, richiede numero intero")
 
if k != "-1" and k.isdigit():  # verifico che non si abbia digitato una lettera ma solo numeri interi e aggiungo in lista
    L.append(k)          # Ciclo con numeri presi in input e inseriti in L fin quando k == -1
while k != "-1":
    k = input("inserire un numero (-1 per terminare): ")
    if not k.isdigit:  # verifico che non si abbia digitato una lettera ma solo numeri interi
        print("errore, richiede numero intero")
        
    if k != "-1" and k.isdigit():   # verifico che non si abbia digitato una lettera ma solo numeri interi e aggiungo in lista
        L.append(k)


# 3
if len(L) == 0:
    print("lista vuota")
else:    
 # 1
    max = L[0]    # variabile max inizializzata con primo elemento in lista
    for i in range(len(L)):   # scandisco la lista e confronto valori con max
        if L[i] > max:
            max = L[i]

    print("Il massimo della lista è:",max)

# 2
    count = 0  # variabile per contare elementi in L
    while True:
        for i in range(len(L)):   # scandisco la lista e incremento contatore
            count+=1
        break    

    print("Il numero degli elementi della lista è:", count)




