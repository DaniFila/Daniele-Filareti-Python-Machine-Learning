import xml.etree.ElementTree as ET
def xml_to_file():
    tree = ET.parse("Corso Python/Martedì 9/file_es5.xml")

    root = tree.getroot()

    return tree,root

def scrivi(root):
    tree = ET.ElementTree(root)
    tree.write("Corso Python/Martedì 9/file_es5.xml")

def verifica():
    try:
        tree,root = xml_to_file()
        vuoto = False
        return tree,root,vuoto
    except:
        vuoto = True
        tree = ""
        root = ""
        return tree,root,vuoto

def menu():
    info_menu = "\n1: Aggiungi studente\n2: Elimina studente\n3: modifica nome studente\n4: aggiungi corso\n5: modifica corso\n6: rimuovi corso\n0: Exit\n"

    scelta_menu = input(info_menu)
    return scelta_menu

def id_nuovo_studente():
    for studente in root.findall("studente"):
        count_id = studente.attrib
    id_nuovo = count_id["id"]
    id_nuovo = int(id_nuovo) + 1
    return id_nuovo

def aggiungi():
    if vuoto:
        root1 = ET.Element("studenti")
        studente = ET.Element("studente",id="0")
        nome_studente = ET.Element("nome")
        nome=input("inserisci nome: ")
        nome_studente.text = nome
        studente.append(nome_studente)
        corsi=ET.Element("corsi")
        a = int(input("Quanti corsi vuoi aggiungere? "))
        for i in range(a):
            corso_nuovo=ET.Element("corso")
            nome_corso = ET.Element("nome")
            nome_corso.text = input("Inserisci nome corso: ")
            voto_corso = ET.Element("voto")
            voto_corso.text = input("Inserire voto corso: ")
            corso_nuovo.append(nome_corso)
            corso_nuovo.append(voto_corso)
            corsi.append(corso_nuovo)
        studente.append(corsi)
        root1.append(studente)
        scrivi(root1)
        print("Studente aggiunto con successo!")
    else:
        id_nuovo = id_nuovo_studente()
        studente = ET.Element("studente",id=str(id_nuovo))
        nome_studente = ET.Element("nome")
        nome=input("inserisci nome: ")
        nome_studente.text = nome
        studente.append(nome_studente)
        corsi=ET.Element("corsi")
        a = int(input("Quanti corsi vuoi aggiungere? "))
        for i in range(a):
            corso_nuovo=ET.Element("corso")
            nome_corso = ET.Element("nome")
            nome_corso.text = input("Inserisci nome corso: ")
            voto_corso = ET.Element("voto")
            voto_corso.text = input("Inserire voto corso: ")
            corso_nuovo.append(nome_corso)
            corso_nuovo.append(voto_corso)
            corsi.append(corso_nuovo)
        studente.append(corsi)
        root.append(studente)
        scrivi(root)
        print("Studente aggiunto con successo!")

def rimuovi():
    trovato = False
    if vuoto:
        print("Il file è vuoto!")
    else:
        studente_S = input("Indicare nome studente da eliminare: ")
        for studente in root.findall("studente"):
            nome = studente.find("nome").text
            if nome == studente_S:
                root.remove(studente)
                trovato = True 
        if not trovato:
            print("Studente non trovato.")
        else:
            print("Studente eliminato con successo!")
            scrivi(root)
    pulisci()
        
def pulisci():
    clear = ET.Element("")
    count = 0
    for studente in root.findall("studente"):
        count+=1
    if count == 0:
        scrivi(clear)

def modifica_studente():
    if vuoto:
        print("Nessun studente presente!")
    else:
        nome = input("Inserisci il nome dell'utente da Modificare: ")
        trovato = False
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome:
                nuovo_nome = input("Inserisci il nuovo nome: ")
                studente.find("nome").text = nuovo_nome
                trovato = True
        if trovato:
            print("Alunno modificato")
            scrivi(root)
        else:
            print("Studente non trovato!")

def aggiungi_corso():
    if vuoto:
        print("Nessun studente presente!")
    else:
        nome = input("Inserisci il nome dell'utente da modificare: ")
        trovato = False
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome and not trovato:
                print("Utente trovato!")
                trovato = True
                corsi = studente.find("corsi")
                corso_nuovo = ET.Element("corso")
                nome_corso = ET.Element("nome")
                nome_corso.text = input("Inserire nome corso nuovo: ")
                voto_corso = ET.Element("voto")
                voto_corso.text = input("Inserire voto corso: ")
                corso_nuovo.append(nome_corso)
                corso_nuovo.append(voto_corso)
                corsi.append(corso_nuovo)
        if trovato:
            print("corso aggiunto con successo!")
            scrivi(root)
        else:
            print("Utente non trovato.")
                
def modifica_corso():
    if vuoto:
        print("Nessun studente presente!")
    else:
        nome = input("Inserisci il nome dell'utente da modificare: ")
        trovato = False
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome and not trovato:
                trovato = True
                print("Utente trovato!")
                corso_S = input("Inserire corso da modificare: ")
                corsi = studente.find("corsi")
                for corso in corsi.findall("corso"):
                    if corso.find("nome").text == corso_S:
                        print("Corso trovato!")
                        select = input("1: modifica nome\n2: modifica voto\n")
                        if select == "1":
                            corso.find("nome").text = input("Inserisci nuovo nome: ")
                        elif select == "2":
                            corso.find("voto").text = input("Inserire voto modificato: ")
                        else:
                            print("Scelta non valida.")
        if trovato:
            print("Modificato con successo!")
            scrivi(root)
        else:
            print("Not Found")

def rimuovi_corso():
    trovato = False
    studente_C = input("Indicare nome studente da eliminare: ")
    for studente in root.findall("studente"):
        nome = studente.find("nome").text
        if nome == studente_C:
            utente = input("Inserisci il corso da eliminare: ")
            corsi = studente.find("corsi")
            for corso in corsi.findall("corso"):
                if corso.find("nome").text == utente and not trovato:
                    trovato = True
                    corsi.remove(corso)
    if trovato:
        print("Il corso è stato eliminato")
        scrivi(root)
    else:
        print("Il corso non è presente!")


while True:
    tree,root,vuoto = verifica()
    scelta_menu = menu()
    if scelta_menu == "1":
        aggiungi()
    elif scelta_menu == "2":
        rimuovi()
    elif scelta_menu == "3":
        modifica_studente()
    elif scelta_menu == "4":
        aggiungi_corso()
    elif scelta_menu == "5":
        modifica_corso()
    elif scelta_menu == "6":
        rimuovi_corso()
    elif scelta_menu == "0":
        break
    else:
        print("Error")












