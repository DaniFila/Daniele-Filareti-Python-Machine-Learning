"""
Dobbiamo creare un programma per la gestione di una biblioteca,
all'avvio del programma ci viene chiesto se siamo amministratori o utenti,
se siamo amministratori possiamo vedere i libri, aggiungere un libro
eliminare un libro.
il libro ha le seguenti caratteristiche:
- titolo
- autore
- anno
- stato prestito
"""
import pickle

def leggi_db_libri():
    with open("Giovedì 27/db_libri.csv", "r") as file:
        db_libri = file.read()
    return db_libri

def leggi_db_utenti():
    with open("Giovedì 27/db_untenti.bin", "rb") as file:
        db_utenti = pickle.loads(file.read())
    return db_utenti


def verifica_db():
    try:
        db_utenti = leggi_db_utenti()
    except:
        psw = {"Amministratori":{"admin":"1234"},"Utenti":{"franco":"0000"}}
        psw_b = pickle.dumps(psw)
        with open("Giovedì 27/db_untenti.bin", "wb") as file:
            file.write(psw_b)
        db_utenti = leggi_db_utenti()   
    libr_vuoti = True
    try:
        db_libri = leggi_db_libri()
    except:
        scrivi_libri("","w")
        db_libri = leggi_db_libri()
    
    if len(db_libri) >0:
        libr_vuoti = False

    return db_utenti , db_libri, libr_vuoti

def scrivi_libri(dato, metodo):
    with open("Giovedì 27/db_libri.csv", metodo) as file:
            file.write(dato)



def inserisci_libro():
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci il autore del libro: ")
    anno = input("Inserisci anno del libro: ")
    stato = "libero"
    nuovo_libro =titolo+","+autore+","+anno+","+stato
    if libr_vuoti:
        scrivi_libri(nuovo_libro, "a")
        
    else:
        scrivi_libri("\n"+nuovo_libro,"a")
    
    print("Libro inserito correttamente!")

def elimina_libro():
    if libr_vuoti:
        print("Nessun libro da eliminare!")
    else:
        titolo = input("Inserisci il titolo del libro: ")
        righe = db_libri.split("\n")
        for riga in righe:
            if titolo == riga.split(",")[0]:
                righe.remove(riga)
                print("Libro eliminato!")
                if len(righe) >1:
                    righe = "\n".join(righe)
                else:
                    righe = "".join(righe)

                scrivi_libri(righe, "w")
            
            else:
                print("Libro non trovato!")
    

def visualizza_libri():
    if libr_vuoti:
        print("Nessun libro!")
    else:
        if len(db_libri) >1:
            righe = db_libri.split("\n")
            for riga in righe:
                riga = riga.split(",")
                print(f"Titolo: {riga[0]}, Autore: {riga[1]}, Anno: {riga[2]}, Stato: {riga[3]}")
        else:
            riga = db_libri.split(",")
            print(f"Titolo: {riga[0]}, Autore: {riga[1]}, Anno: {riga[2]}, Stato: {riga[3]}")

def aggiungi_amministratore():
    nome_utente = input("Inserire nome utente")
    psw = input("Inserire la password nel nuovo admin: ")
    db_utenti["Amministratori"][nome_utente] = {}
    db_utenti["Amministratori"][nome_utente] = psw
    psw_b = pickle.dumps(db_utenti)
    with open("Giovedì 27/db_untenti.bin", "wb") as file:
        file.write(psw_b)
    leggi_db_utenti()
    print("Admin inserito correttamente")

def aggiungi_utente():
    nome_utente = input("Inserire nome utente")
    psw = input("Inserire la password nel nuovo utente: ")
    db_utenti["Utenti"][nome_utente] = {}
    db_utenti["Utenti"][nome_utente] = psw
    psw_b = pickle.dumps(db_utenti)
    with open("Giovedì 27/db_untenti.bin", "wb") as file:
        file.write(psw_b)
    leggi_db_utenti()
    print("Utente inserito correttamente")

def login():
    tipo_utente = input("Inserisci 1 per amministratore\n2 per utente: ")
    return tipo_utente

def menu_admin():
    info_menu="""Inserisci 1 per inserire un libro\n
Inserisci 2 per eliminare libro\n
Inserisci 3 per visualizzare i libri\n
Inserisci 4 per aggiungere utenti amministratori\n
Inserisci 5 per aggiungere utenti normali """
    scelta_menu = input(info_menu)

    return scelta_menu

def menu_utente():
    info_menu="""Inserisci 1 per visualizzare libri\n
Inserisci 2 per prendere un libro in prestito se è libero\n
Inserisci 3 per restituire un libro\n """
    scelta_menu = input(info_menu)
    return scelta_menu

def prestito():
    if libr_vuoti:
        print("Nessun libro")
    else:
        libro = input("Indicare libro: ")
        if len(db_libri) >1:
            righe = db_libri.split("\n")
            for lib0 in range(len(righe)):
                print(righe[lib0])
                if righe[lib0][0] == libro:
                    if righe[lib0][len(righe[lib0])-1] == "libero":
                        righe[lib0].replace("libero","prestito")
                        print("libro prestato con successo!")
                        scrivi_libri(righe,"w")
        else:
            riga = db_libri.split(",")
            for lib0 in range(len(riga)):
                if riga[0] == libro:
                    if riga[len(riga)-1] == "libero":
                        riga.replace("libero","prestito")
                        print("libro prestato con successo!")
                        scrivi_libri(riga,"w")


                    
        



    

db_utenti , db_libri, libr_vuoti =verifica_db()

print("Benvenuto nella biblioteca\n")

tipo_utente = login()
if tipo_utente == "1":
    nome_utente_input = input("Inserire nome utente: ")
    password_input = input("Inserisci password: ")
    if nome_utente_input in db_utenti["Amministratori"]:
        if db_utenti["Amministratori"][nome_utente_input] == password_input:
            scelta_menu = menu_admin()
            if scelta_menu == "1":
                inserisci_libro()
            elif scelta_menu == "2":
                elimina_libro()
            elif scelta_menu == "3":
                visualizza_libri()
            elif scelta_menu == "4":
                aggiungi_amministratore()
            elif scelta_menu == "5":
                aggiungi_utente()
elif tipo_utente == "2":
    nome_utente_input = input("Inserire nome utente: ")
    password_input = input("Inserisci password: ")
    if nome_utente_input in db_utenti["Utenti"]:
        if db_utenti["Utenti"][nome_utente_input] == password_input:
            scelta_menu = menu_utente()
            if scelta_menu == "1":
                visualizza_libri()
            elif scelta_menu == "2":
                prestito()

        


        




    