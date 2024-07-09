import xml.etree.ElementTree as ET

def xml_to_file():
    tree = ET.parse("Corso Python/Martedì 9/file_es3.xml")

    root = tree.getroot()

    return tree,root


tree,root = xml_to_file()


def aggiungi_libro(root):
    libro = ET.Element("libro")
    titolo_libro = input("Inserire titolo del libro: ")
    autore_libro = input("Inserire autore del libro: ")
    titolo = ET.Element("titolo")
    autore = ET.Element("autore")
    titolo.text = titolo_libro
    autore.text = autore_libro
    libro.append(titolo)
    libro.append(autore)
    root.append(libro)
    

aggiungi_libro(root)

tree.write("Corso Python/Martedì 9/file_es3.xml")

