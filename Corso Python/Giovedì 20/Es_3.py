

print("\nMENU'")
print("")
print("Verificare numero o stringa pari o dispari: 1")
print("Numeri primi in un intervallo: 2")
print("Verifica fattori comuni: 3")
print("Exit: -1")
print("")


v = "SI"

while True:
    A = input("Seleziona azione: ")    # per indicare operazione

    if A == "1":     # se A == 1
        while v == "SI":
            q = input("Selezionare Stringa o Intero - (S/I): ")    # richiesta stringa o intero 
            if q == "S":
                q = input("inserire stringa: ")    # se stringa si inserisce stringa
                if len(q) %2 == 0:
                    print("La Stringa è pari.")   # si verifica lunghezza e si divide per 2 e si controlla il resto
                else:
                    print("La stringa è dispari.")
            elif q == "I":
                q = int(input("inserire l'intero: "))   # se intero si inserisce intero
                if q%2 == 0:
                    print("Il numero è pari.")    # si verifica il resto della divisione per 2
                else:
                    print("Il numero è dispari.")
            else: 
                print("Non valido")    # se si indica un valore diverso tra S e I
            print("Vuoi ripetere? (SI per ripetere): ")
            v = input("Inserire scelta: ")     # si indica la scelta per continuare

    elif A == "2":
        a = int(input("Indicare estremo sinistro: "))   # si indicano gli estremi sinistri e destri
        z = int(input("Indicare estremo destro: "))
        d = input("indicare con 1 i numeri primi, 0 altrimenti: ")   # si indica se visualizzare numeri primi nel range o numeri non primi
        if d == "1":
            for i in range(a,z+1):
                if i%2 !=0:
                    print(i)         #in base alla scelta si scandisce il range e si verifica numero per volta
        elif d == "0":
            for i in range(a,z+1):
                if i%2 ==0:
                    print(i)
        else:
            print("operazione non valida")                       


    elif A == "-1":        # Se si indica -1 si esce
        break        
                       
