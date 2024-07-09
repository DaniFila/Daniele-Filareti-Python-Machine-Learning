import xml.etree.ElementTree as ET

def xml_to_file():
    tree = ET.parse("Corso Python/Martedì 9/path_to_file.xml")

    root = tree.getroot()

    return tree,root

def xml_to_string():
    xml_data = '''<?xml version="1.0"?>
    <saluti>
    <saluto>Hello World</saluto>
    </saluti>'''

    root = ET.fromstring(xml_data)
    tree = ET.ElementTree(root)
    return tree,root


tree,root = xml_to_file()

# root = xml_to_string()

#for saluto in root.findall('saluto'):
    #print(saluto.text)

new_element = ET.Element('nuovo_tag')

new_element.text = "testo del nuovo elemento"

root.append(new_element)

tree.write("Corso Python/Martedì 9/file.xml")