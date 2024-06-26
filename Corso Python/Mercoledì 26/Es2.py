def estrai_file():
    with open("Mercoledì 26/Es2.txt","r") as f:
        file = f.read()
    return file
def righe_in_lista(f):
    l = f.split("\n")
    return l
def conta_parole(f):
    count = 0
    for parola in f:
        count+=parola
    return count
def conta_caratteri(f):
    h = " "
    count = 0
    for riga in f:
        for parola in riga:
            if parola not in h:
                count+=1
    return count

    
#with open("Mercoledì 26/Es2.txt","w") as file:
    file.write("""Cos’è Lorem Ipsum?
Lorem Ipsum è un testo segnaposto utilizzato
nel settore della tipografia e della stampa. 
Lorem Ipsum è considerato il testo segnaposto 
standard sin dal sedicesimo secolo, quando un 
anonimo tipografo prese una cassetta di caratteri
e li assemblò per preparare un testo campione. 
È sopravvissuto non solo a più di cinque secoli, 
ma anche al passaggio alla videoimpaginazione, 
pervenendoci sostanzialmente inalterato. 
Fu reso popolare, negli anni ’60, con la 
diffusione dei fogli di caratteri trasferibili 
“Letraset”, che contenevano passaggi del 
Lorem Ipsum, e più recentemente da software 
di impaginazione come Aldus PageMaker, che includeva versioni 
del Lorem Ipsum.
Da dove viene?
Al contrario di quanto si pensi, Lorem Ipsum non è semplicemente
una sequenza casuale di caratteri. Risale ad un classico della 
letteratura latina del 45 AC, cosa che lo rende vecchio di 2000 anni. 
Richard McClintock, professore di latino al Hampden-Sydney College in Virginia,
ha ricercato una delle più oscure parole latine, consectetur, da un passaggio 
del Lorem Ipsum e ha scoperto tra i vari testi in cui è citata, la fonte da 
cui è tratto il testo, le sezioni 1.10.32 and 1.10.33 del "de Finibus Bonorum et Malorum"
di Cicerone. Questo testo è un trattato su teorie di etica, molto popolare nel Rinascimento. 
La prima riga del Lorem Ipsum, "Lorem ipsum dolor sit amet..", è tratta da un passaggio della sezione 1.10.32. Il brano standard del Lorem Ipsum usato 
sin dal sedicesimo secolo è riprodotto qui di seguito per coloro 
che fossero interessati. Anche le sezioni 1.10.32 e 1.10.33 del "de Finibus Bonorum et Malorum" di Cicerone 
sono riprodotte nella loro forma originale, accompagnate dalla traduzione inglese del 1914 di H. Rackham.""")
    


file = estrai_file()
file_diviso_righe = righe_in_lista(file)
n_righe = len(file_diviso_righe)
n_caratteri = conta_caratteri(file_diviso_righe)
n_parole = conta_parole(file_diviso_righe)

print("Il numero di righe è",n_righe)
print("Il numero di caratteri è", n_caratteri)
print("Il numero di parole è",n_parole)






    