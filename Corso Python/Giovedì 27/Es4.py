"""Create un programma per la gestione di una biblioteca, il programma può avere 2 tipi di utenti:
- utente amministratore può:
-vedere i libri presenti e se sono
in prestito o disponibili
-eliminare o aggiungere un libro"""
import csv
def leggi_file(file_path):
    # Legge il file CSV e ritorna una lista di liste con i dati dei libri
    database = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            database.append(row)
    return database
def scrivi_file(file_path, database):
    # Scrive i dati del database nel file CSV
    with open(file_path, 'w', newline='') as file:
        file.writelines(str(database))
def aggiungi_libro(biblioteca, titolo):
    if titolo in biblioteca:
        print(f"il libro '{titolo}' è già presente nella biblioteca. ")
        # indicare che il libro è disponibile
    else:
        biblioteca["titolo"] = titolo
        print(f"il libro '{titolo}' è stato aggiunto alla biblioteca")

    return biblioteca
def menù_accesso():
    print("")
    print("ACCESSO")
    print("Admin: 1")
    print("Utente: 2")
    print("Exit: 3")
def menù_admin():
    print("Menù Amministratore")
    print("Visualizza libri: 1")
    print("Aggiungere libro: 2")
    print("Elimina libro: 3")
    print("")
def verifica_esistenza_database():
    try:
        database = leggi_file("Giovedì 27/Es4.txt")
    except:
        scrivi_file("Giovedì 27/Es4.txt",database)

    return database

database = {"titolo":"disponibile","titolo2":"prestato"}

accesso_admin = False
accesso_utente = False
amministratori = {"pippo":"1234","franco":"0000","admin":"admin"}
utenti = {"tonino":"blu123","giuseppe":"1212","micheal":"gg2211"}
while not accesso_admin and not accesso_utente:
    menù_accesso()
    z = input("Indicare selezione: ")
    if z == "1":
        nome_utente = input("Indicare nome utente: ")
        while not nome_utente.isalpha():
            nome_utente = input("Indicare nome utente valido:")
        password = input("Indicare la password: ")
        if nome_utente in amministratori:
            if amministratori[nome_utente] == password:
                accesso_admin = True
                print("Benvenuto amministratore")
            else:
                print("Password errata")
        else:
            print("Nome utente errato")
    elif z == "2":
        nome_utente = input("Indicare nome utente: ")
        while not nome_utente.isalpha():
            nome_utente = input("Indicare nome utente valido: ")
        password = input("Indicare la password: ")
        if nome_utente in utenti:
            if utenti[nome_utente] == password:
                accesso_utente = True
                print("Benvenuto utente")
            else:
                print("Password errata")
        else:
            print("Nome utente errato")
    elif z == "3":
        print("Arrivederci")
        break
    else:
        print("selezione non valida")

"""while accesso_admin:
    menù_admin
    h = input("seleziona opzione: ")
    if h == "1":"""

scrivi_file("Giovedì 27/Es4.csv",database)