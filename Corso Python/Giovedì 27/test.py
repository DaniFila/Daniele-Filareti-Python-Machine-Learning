nome = "tommaso"

voti = "6 10 7"

lista_voti = voti.split(" ")



stringa_voti_archiviati = "-".join(lista_voti)

#print(stringa_voti_archiviati)

stringa_alunno = nome+","+stringa_voti_archiviati

print(stringa_alunno)