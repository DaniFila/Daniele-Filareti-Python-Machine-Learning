database1 = {"daniele":"1234",
            "pippo": "0000"}

database2 = {"daniele": "viola",           ## 3 Database contenenti informazioni nome utente, password e preferenze animali e colori
             "pippo": "blu"}

database3 = {"daniele": "corso",
             "pippo": "carlino"}

# in input richiediamo dati utente
nome_utente = input("Inserire nome utente ")   
pasw = input("inserire la password ")



if nome_utente in database1:      # verifico nome utente in database
    t = database1.get(nome_utente)      # se si verifico password nome utante
    if t == pasw: 
        print("Benvenuto! ")
        print("seleziona azione")
        print("colore preferito 1")
        print("animale preferito 2")
        print("")
        n = input("indica azione")               
        if n == "1":
            s = input("qual è il tuo colore preferito? ")
            if s == database2.get(nome_utente):
                print("accesso consentito")
            else:                                                      # se nome utente e password corrispondono, verifica ulteriore preferenze animale o colore, scelto dall'utente
                print("accesso negato")  
        elif n == "2":
            v = input("qual è il tuo animale preferito? ")
            if v == database3.get(nome_utente):
                print("accesso consentito")
            else:
                print("accesso negato ")            
        else:
            print("azione negata")        
    else:
        print("password errata ")                # se password errata
else:
    print("nome utente non presente in database")       # se nome utente non presente



