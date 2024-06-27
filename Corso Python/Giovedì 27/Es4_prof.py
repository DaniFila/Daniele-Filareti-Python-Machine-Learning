import pickle



def leggi_db_libri():
    with open("Giovedì 27/db_libri.csv","r") as file:
        db_libri = file.read()
    return db_libri

def leggi_db_utenti():
    with open("Giovedì 27/db_utenti.bin","rb") as file:
        db_utenti = pickle.loads(file.read())
    return db_utenti



def verifica_db():
    try:
        db_utenti = leggi_db_utenti()
    except:
        psw = "1234"
        psw_b = pickle.dumps(psw)
        with open("Giovedì 27/db_utenti.bin","wb") as file:
            file.write(psw_b)
        db_utenti = leggi_db_utenti()
    libr_vuoti = True
    try:
        db_libri = leggi_db_libri()
    except:
        scrivi_libri("")
        db_libri = leggi_db_libri()
    
    if len(db_libri) > 0:
        libr_vuoti = False
    
    return db_utenti,db_libri,libr_vuoti

def scrivi_libri(dato,metodo):
    with open("Giovedì 27/db_libri.csv",metodo) as file:
            file.write(dato)
#verifica_db()

def inserisci_libro():
    titolo = input("inserisci il titolo del libro: ")
    autore = input("inserisci autore del libro: ")
    anno = input("inserisci anno del libro: ")
    stato = "libero"

    nuovo_libro = titolo+","+autore+","+anno+","+stato
    if libr_vuoti:
        scrivi_libri(nuovo_libro,"a")
    else:
        scrivi_libri("\n"+nuovo_libro)
    print("libro inserito correttamente")

def elimina_libro():
    if libr_vuoti:
        print("Nessun libro da eliminare")
    else:    
        titolo = input("inserire il titolo del libro: ")
        righe = db_libri.split("\n")
        for riga in righe:
            if titolo == riga.split(",")[0]:
                righe.remove(riga)
                print("Libro eliminato")
                if len(righe) >1:
                    righe = "\n".join(righe)
                else:
                    righe = "".join(righe)
                scrivi_libri(righe,"w")
            else:
                print("libro non trovato")

  

def visualizza_libri():
    if libr_vuoti:
        print("Nessun libro")
    else:
        if len(db_libri) >1:
            righe = db_libri.split("\n")
            for riga in righe:
                riga = riga.split(",")
                print("Titolo:",riga[0],"Autore:",riga[1],"Anno:",riga[2],"Stato:",riga[3])
        else:
            riga = db_libri.split(",")
            print("Titolo:",riga[0],"Autore:",riga[1],"Anno:",riga[2],"Stato:",riga[3])
def login():
    tipo_utente = input("Inserisci 1 per amministratore\n2 per utente: ")
    return tipo_utente
def menu():
    info_menu = "Inserisci 1 per inserire un libro \n inserisci 2 per eliminare libro\n inserisci 3 per visualizzare i libri"
    scelta_menu = input("Benvenuto nella biblioteca")
    return scelta_menu

db_utenti , db_libri , libr_vuoti = verifica_db()

print("Benvenuto nella biblioteca\n")

tipo_utente = login()
if tipo_utente == "1":
    password_input = input("Inserisci password: ")
    if password_input == db_utenti:
        scelta_menu = menu()
        if scelta_menu == "1":
            inserisci_libro()
        elif scelta_menu == "2":
            elimina_libro()
        elif scelta_menu == "3":
            visualizza_libri()
        