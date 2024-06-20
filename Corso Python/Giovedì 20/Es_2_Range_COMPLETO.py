# MENU'

print("\nBENVENUTO")
print("")
print("Verifica numero Pari o Dispari: 1")
print("Sequenza di numeri da 0 a N preso da input: 2")
print("Quadrato di una lista di numeri: 3")
print("Analisi lista presa in input: 4")
print("EXIT: -1 ")
print("")

while True:
    Z = input("Indicare Scelta: ")

    if Z == "1":
        N = int(input("inserire un numero (verifico se pari o dispari): "))  # si richiede il numero

        if N%2 == 0:  # si verifica il resto della divisione per 2, se 0 allora è pari, dispari altrimenti
            print("Pari")
        else:
            print("Dispari")

    if Z == "2":
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
    if Z == "3":
        L = [] # lista per inserire numeri da input
        L2 = [] # lista contenente tutti i numeri presi in input al quadrato
        h = int(input("inserire un numero (-1 per terminare): "))  
        if h != -1:
            L.append(h)          # Ciclo con numeri presi in input e inseriti in L fin quando k == -1
        while h != -1:
            h = int(input("inserire un numero (-1 per terminare): "))
            if h != -1:
                L.append(h)



        for i in range(len(L)):   # scorrimento della lista L e per ogni numero si fa il quadrato e si aggiunge in L2
            L2.append(L[i]*L[i])

        print("LISTA INIZIALE")
        print(L)
                                # Stampe finali delle 2 liste
        print("")

        print("LISTA FINALE")
        print(L2)
    if Z == "4":
        list = [] # lista per inserire numeri da input
        x = input("inserire un numero (-1 per terminare): ")
        if not x.isdigit():    # verifico che non si abbia digitato una lettera ma solo numeri interi
            print("errore, richiede numero intero")
 
        if x != "-1" and x.isdigit():  # verifico che non si abbia digitato una lettera ma solo numeri interi e aggiungo in lista
            list.append(x)          # Ciclo con numeri presi in input e inseriti in L fin quando k == -1
        while x != "-1":
            x = input("inserire un numero (-1 per terminare): ")
            if not x.isdigit():  # verifico che non si abbia digitato una lettera ma solo numeri interi
                print("errore, richiede numero intero")
        
            if x != "-1" and x.isdigit():   # verifico che non si abbia digitato una lettera ma solo numeri interi e aggiungo in lista
                list.append(x)


        # 3
        if len(list) == 0:
            print("lista vuota")
        else:    
        # 1
            max = list[0]    # variabile max inizializzata con primo elemento in lista
            for i in range(len(list)):   # scandisco la lista e confronto valori con max
                if list[i] > max:
                    max = list[i]

            print("Il massimo della lista è:",max)

        # 2
            count = 0  # variabile per contare elementi in L
            while True:
                for i in range(len(list)):   # scandisco la lista e incremento contatore
                    count+=1
                break    

            print("Il numero degli elementi della lista è:", count)
    if Z == "-1":
        break            


