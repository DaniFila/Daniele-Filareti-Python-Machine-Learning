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
    info_menu = """Inserisci 1 per aggiungere numero\n
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
    