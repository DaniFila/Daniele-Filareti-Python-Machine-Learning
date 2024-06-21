start = True
database_clienti = {"pippo":"1234",
                    "baudo":"3214",
                    "franco":"0000"}


print("\nBenvenuto")
print("Eseguire login 1: ")
print("Effettuare Registrazione 2: ")
print("Exit (qualsiasi comando): ")
print("")

while start:
    f = input("indicare azione: ")
    if f == "1":
        username = input("indicare nome utente ")          # si richiede in input username
        pasw = input("indicare la password ")               # si richiede in input password
        if username in database_clienti:        # si verifica se username si trova in dizionario 
            if database_clienti[username] == pasw:     # se si, si confronta username con password nel dizionario e si verifica se corrispondono
                print("")
                utente = True 

                print("\nMenu'")
                print("Punto 1: ")
                print("Punto 2: ")
                print("Punto 3: ")
                print("Punto 4: ")
                print("Exit: (qualsiasi tasto): ")



                # PUNTO 1
                while True:
                    Z = input("Indicare la scelta:")
                    if Z == "1":

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

                    elif Z == "2":

                        stringa = input("Inserire una stringa: ")   # stringa da input

                        for i in range(len(stringa)):  # scan della stringa con il len della string
                            print(stringa[i])  # stampa di ciascun carattere

#----------------------------------------------

                    # PUNTO 3
                    elif Z == "3":
                        N = int(input("Indicare massimo numero range: "))
                        S = int(input("indicare lo step per il range: "))

                        for i in range(0,N,S):
                            print(i)
#------------------------------------------------
#                   # PUNTO 4                            
                    elif Z == "4":
                        primo = True  #variabile per verifica primo
                        n = int(input("indicare numero da verificare: ")) #richiesta numero primo
                        for i in range(2,n-1):
                            if n%i==0:    #scan per verifica divisori di n
                                primo = False
                        if primo:
                            print("Il numero è primo")   # stampe dopo verifica 
                            print("")
                        else:
                            print("Il numero non è primo")
                            print("")            
                    else:
                        print("")
                        print("Eseguire login 1: ")
                        print("Effettuare Registrazione 2: ")
                        print("Exit (qualsiasi comando): ")
                        print("")
                        break


        else:
            print("Credenziali errate")
    elif f == "2":
        username = input("indicare nome utente: ")
        pasw = input( "indicare la password: ")
        database_clienti[username] = pasw

    else:
        start = False    