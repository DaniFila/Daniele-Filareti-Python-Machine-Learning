# Inventario inizializzato con prodotti
inventario = ["pane","frutta","verdura","acqua","pasta"]
# dizionario con prodotti e prezzo
listino = {"pane": 4,
           "frutta": 2,
           "verdura": 3,
           "acqua": 1,
           "pasta": 5}
# dizionario con prodotti e numero disponibili
disponibilità = {"pane": 7,
           "frutta": 10,
           "verdura": 2,
           "acqua": 17,
           "pasta": 0}
prodotti_cliente = [] # lista per prodotti del cliente
a = int(input("Vuoi avviare il sistema? (1 per SI, 0 per NO)"))
if a == 1:
    while True:
        print("Visualizza inventario: 1")
        print("acquista articoli: 2")
        print("visualizza inventario utente: 3")
        print("aggiungi articolo in inventario: 4")
        print("rimuovi articoli dall'inventario: 5")
        print("aggiorna listino e disponibilità: 6")
        print("visualizza listino e disponibilità: 7")
        print("numero diverso per uscire: ")
        print("")
        c = input("Seleziona azione: ")
        print("")
        if c == "1":    # visualizza inventario
            print(inventario)
        elif c == "2":   # per acquistare articolo
            articolo = input("indicare articolo da acquistare ")   #si indica l'articolo dall'input
            print("")
            if articolo in inventario:      #si verifica se presente
                if disponibilità.get(articolo) != 0:       #si verifica se disponibile
                    prodotti_cliente.append(articolo)
                    disponibilità[articolo]-=1    #si scalcola una quantità dalla disponibilità del prodotto
                else:
                    print("prodotto non disponibile")    # mess per prodotto non disponibile oppure scritto male
                    print("")
        elif c == "3":  # visualizza prodotti acquistati dal cliente
            print(prodotti_cliente)
        elif c == "4":   # aggingi articolo in inventario
            prodotto_nuovo = input("inserire nuovo prodotto ")      #nome prodotto nuovo
            prezzo_prodotto_nuovo = int(input("indicare il prezzo "))   # prezzo del prodotto nuovo
            quantità_prodotto_nuovo = int(input("indicare quantità "))   # quantità del prodotto nuovo
            inventario.append(prodotto_nuovo)   # si aggiunge prodotto nuovo in inventario
            listino[prodotto_nuovo] = prezzo_prodotto_nuovo   # si aggiunge il prodotto nel listino col suo prezzo
            disponibilità[prodotto_nuovo] = quantità_prodotto_nuovo # si aggiunge il prodotto nella disponibilità con la sua quantità
        elif c == "5":   # rimuovere articolo
            prodotto = input("indicare prodotto ")   # si indica l'articolo da rimuovere
            if prodotto in inventario:  # se presente nell'inventario
                inventario.remove(prodotto)   # si rimuove dalla lista inventario
                listino.pop(prodotto)    # si rimuove dal listino
                disponibilità.pop(prodotto)   # si rimuove dalla disponibilità
                print(listino)   
                print("")           # qui ho stampato i 2 dizionari per verificare il cambiamento
                print(disponibilità)
            else:
                print("prodotto assente")  # se il prodotto è assente
        elif c == "6":  # aggiornare listino e disponibilità
            print(listino)
            print("")                 # stampa per visualizzare e gestire meglio la scelta della modifica
            print(disponibilità)
            print("")
            prodotto1 = input("indicare prodotto ")   # si indica il prodotto
            if prodotto1 in inventario:  # se presente
                prezzo = int(input("indicare nuovo prezzo "))  # si indica nuovo prezzo
                quantità = int(input("indicare nuova quantià "))  # si indica nuova quantità
                listino[prodotto1] = prezzo  # si aggiorna il prezzo
                disponibilità[prodotto1] = quantità   # si aggiorna la quantità
            else:
                print("prodotto assente")    # se il prodotto è assente
        elif c == "7":
            print("LISTINO")
            print(listino)   
            print("")           # visualizza listino e disponibilità
            print("DISPONIBILITà")
            print(disponibilità)        
            print("")



        
        else:
            break  # se il numero selezionato è diverso da quelli indicati si chiude il ciclo
                    


                    



