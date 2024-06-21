somma_numeri_dispari = 0   # contatore somma numeri dispari
tentativi = 0   # contatore tentativi
while somma_numeri_dispari < 250 and tentativi < 3:  # ciclo fin quando non si supera 250 oppure si terminano tentativi
    tentativi+=1 
    n = int(input("Inserire numero intero positivo: "))   # si inserisce l'intero
    while n < 0:
        n = int(input("Inserire numero intero positivo: "))  # se non è positivo si ripete fin quando non si inserisce uno positivo
    somma_numeri_dispari = 0
    for i in range(n+1):   # si verifica il range del numero e si stampano i numeri pari nel range
        if i%2 == 0:  
            print(i)
        else:
            somma_numeri_dispari+=i   # se è dispari si somma nella variabile
    if somma_numeri_dispari < 250:
        print("la somma dei numeri nel range dispari è:", somma_numeri_dispari, "Riprovare")    # se la somma è minore di 250 allora si deve riprovare
    else:
        print("Hai vinto!")    # se si supera 250 si vince

if somma_numeri_dispari < 250:  # se alla conclusione del ciclo non si vince allora messaggio finito i tentativi 
    print("Hai finito i tentativi")       
