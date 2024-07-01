def lettura():     # Funzione per lettura file e salvataggio del contenuto per utilizzo nel programma
    with open("Lunedì 1/Es1.csv","r") as file:
        a = file.read()

    return a

def scrittura(s,mod):   # Funzione che permette la scrittura su file in modalità scelta dall'utente e stringa data
    with open("Lunedì 1/Es1.csv",mod) as file:
        file.write(s)

def verifica_db():  # Funzione che verifica esistenza del file per poterlo copiare nel programma all'utilizzo ed eventualmente crea file vuoto e restituisce con una verifica un booleano che indica se il file contiene dati
    db_vuoto=True
    try:
        db=lettura()
        if len(db)>1:
            db_vuoto = False
    except :
        db=scrittura("","w")


    return db,db_vuoto

def menu(): # Funzione che stampa le operazione che si possono svolgere nel programma con selezione e ritorno del valore indicato dall'utente
    info_menu = """\nInserisci 1 per aggiungere numero\n
Inserisci 2 per visualizzare rubrica\n
Inserisci 3 per eliminare numero dalla rubrica\n
Inserisci 4 per uscire\n"""

    scelta_menu = input(info_menu)
    
    return scelta_menu

def aggiungi(): #Funzione che permette l'inserimento nella rubrica telefonica un nuovo numero di telefono formattato con nome,cognome,numero nel file
    nome = input("Inserire nome: ")
    cognome = input("Inserire cognome: ")
    num = input("Inserire numero di telefono: ")
    dato = nome+","+cognome+","+num+"\n"
    scrittura(dato,"a")
    print("\nNumero inserito con successo!")

def visualizza(): # Funzione che permette di visualizzare il contenuto della rubrica facendo dei controlli sulla lunghezza per dividere le righe in lista e per ogni riga separare i dati dalla virgola per poterli andare a stampare con l'indice della lista della riga, se il file contiene solo una riga si divide dalle virgole e si stampa
    if db_vuoto:
        print("Non ci sono numeri in rubrica")
    else:
        if len(db) >1:
            righe = db.split("\n")
            for riga in righe:
                riga = riga.split(",")
                if riga[0].isalpha():
                    print(riga[0],riga[1],riga[2])
        else:
            riga = db.split(",")
            print(riga[0],riga[1],riga[2])

def elimina(): # Funzione che permette di ricercare un numero di telefono per eliminarlo prendendo i dati nel file scomponendo le righe e successivamente ricompattarlo in stringa
    trov = False
    if db_vuoto:
        print("La rubrica è vuota!")
    else:
        numero = input("Indicare numero di telefono da eliminare: ")
        righe = db.split("\n")
        for riga in righe:
            if numero == riga.split(",")[2]:
                righe.remove(riga)
                print("Libro eliminato!")
                trov = True
                if len(righe) >1:
                    righe = "\n".join(righe)
                else:
                    righe = "".join(righe)

                scrittura(righe, "w")
            
            elif not trov:
                print("Numero non trovato!")
                
while True: # Ciclo dove vengono richiamate le varie funzioni partendo dal menu e verificando la scelta dell'utente effettuando le varie operazioni
    db,db_vuoto = verifica_db()
    scelta_menu = menu()
    if scelta_menu == "1":
        aggiungi()
    elif scelta_menu == "2":
        visualizza()
    elif scelta_menu == "3":
        elimina()
    elif scelta_menu == "4":
        print("Arrivederci")
        break
    else:
        print("Scelta non valida")


