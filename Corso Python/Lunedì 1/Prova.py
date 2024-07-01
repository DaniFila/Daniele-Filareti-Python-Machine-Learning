def lettura():     # Funzione per lettura file e salvataggio del contenuto per utilizzo nel programma
    with open("Lunedì 1/Es1.py","r") as file:
        a = file.read()

    return a

def scrittura(s,mod):   # Funzione che permette la scrittura su file in modalità scelta dall'utente e stringa data
    with open("Lunedì 1/Es1.py",mod) as file:
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