import xml.etree.ElementTree as ET

def xml_to_file():
    tree = ET.parse("Corso Python/Martedì 9/file_es4.xml")

    root = tree.getroot()

    return tree,root


tree,root = xml_to_file()
def search_print(root):
    p = int(input("indicare filtro prezzo: "))
    for prodotto in root.findall("prodotto"):
        nome = prodotto.find("nome").text
        prezzo = prodotto.find("prezzo").text
        if int(prezzo) <= p:
            print(f"Prodotto: {nome}, prezzo: {prezzo}")



search_print(root)
    

