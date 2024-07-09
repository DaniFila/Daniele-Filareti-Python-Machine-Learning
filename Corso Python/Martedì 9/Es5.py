import xml.etree.ElementTree as ET
def xml_to_file():
    tree = ET.parse("Corso Python/Martedì 9/file_es5.xml")

    root = tree.getroot()

    return tree,root

def scrivi(tree):
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
    info_menu = "1: Aggiungi studente\n2: Elimina studente\n3: modifica studente\n"

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
        tree = ET.ElementTree(root1)
        return tree
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
        tree = ET.ElementTree(root)
        return tree

def rimuovi():
    if vuoto:
        print("Il file è vuoto!")
    else:
        stud = input("")

tree,root,vuoto = verifica()


        
            







