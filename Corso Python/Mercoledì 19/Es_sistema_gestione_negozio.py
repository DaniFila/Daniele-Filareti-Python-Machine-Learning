inventario = ["pane","frutta","verdura","acqua","pasta"]
amministratori = {"daniele": "1234",
                  "pippo": "0000"}
listino = {"pane": 4,
           "frutta": 2,
           "verdura": 3,
           "acqua": 1,
           "pasta": 5}

disponibilità = {"pane": 7,
           "frutta": 10,
           "verdura": 2,
           "acqua": 17,
           "pasta": 0}

vendite = {}
prodotti_cliente = []
a = int(input("Vuoi avviare il sistema? (1/0)"))
if a == 1:
    login = input("vuoi entrare come admin? (1/0) ")                           ## per il tempo ho incasinato la indentazione, devo sistemarla domani
                                                                              ## devo sistemare alcune cose 
    while login == 1:
        username = input("indicare nome utente ")
        pasw = input("indicare la password")
        if username in amministratori:
            if amministratori[username] == pasw:
                print("benvenuto amministratore")
                print("")
                print("seleziona azione")
                print("rapporto delle vendite: 1")
                print("visualizza stato corrente inventario: 2")
                print("numero diverso per uscire")
                azione_admin = input("indicare azione: ")
                if azione_admin == 1:
                    print(vendite)
                elif azione_admin == 2:
                    print(inventario)
                else:
                    print("azione non valida") 
                    if login == 0:
        print("Visualizza inventario: 1")
        print("acquista articoli: 2")
        print("visualizza inventario utente: 3")
        print("aggiungi articolo in inventario:4")
        print("rimuovi articoli dall'inventario: 5")
        print("aggiorna listino e disponibilità: 6")
        print("numero diverso per uscire")
        print("")
        c = input("Seleziona azione: ")
        print("")
        if c == "1":
             print(inventario)
        elif c == "2":
            articolo = input("indicare articolo da acquistare ") 
            print("")
            if articolo in inventario:
                if disponibilità.get(articolo) != 0:
                    prodotti_cliente.append(articolo)
                    disponibilità[articolo]-=1
                    vendite[articolo] += 1
                else:
                    print("prodotto non disponibile")
                    print("")
        elif c == "3":
            print(prodotti_cliente)
        elif c == "4":
            prodotto_nuovo = input("inserire nuovo prodotto ")
            prezzo_prodotto_nuovo = int(input("indicare il prezzo ")) 
            quantità_prodotto_nuovo = int(input("indicare quantità "))
            inventario.append(prodotto_nuovo)   
            listino[prodotto_nuovo] = prezzo_prodotto_nuovo
            disponibilità[prodotto_nuovo] = quantità_prodotto_nuovo
        elif c == "5":
            prodotto = input("indicare prodotto ")
            if prodotto in inventario:
                inventario.remove(prodotto)
                listino.pop(prodotto)
                disponibilità.pop(prodotto)
                print(listino)
                print("")
                print(disponibilità)
            else:
                print("prodotto assente")
        elif c == "6":
            print(listino)
            print("")
            print(disponibilità)
            print("")
            prodotto1 = input("indicare prodotto ")
            if prodotto1 in inventario:
                prezzo = int(input("indicare nuovo prezzo "))
                quantità = int(input("indicare nuova quantià "))
                listino[prodotto1] = prezzo
                disponibilità[prodotto1] = quantità
            else:
                print("prodotto non disponibile")    
        else: 
         a == 0


        
                    


                    



