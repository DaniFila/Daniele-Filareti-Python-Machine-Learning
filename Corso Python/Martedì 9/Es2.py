import xml.etree.ElementTree as ET

studenti = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]


root = ET.Element("Studenti")

for element in studenti:
    elemento_studente = ET.Element("studente")
    for chiave,valore in element.items():
        nuovo_elemento = ET.Element(chiave)
        nuovo_elemento.text= valore
        elemento_studente.append(nuovo_elemento)
    root.append(elemento_studente)



tree = ET.ElementTree(root)

tree.write("Corso Python/Martedì 9/file_es2.xml")