import xml.etree.ElementTree as ET
def xml_to_string():
    xml_data = '''<studenti>
<studente>
<nome>Alice</nome>
<eta>22</eta>
</studente>
<studente>
<nome>Bob</nome>
<eta>25</eta>
</studente>
</studenti>'''

    root = ET.fromstring(xml_data)
    tree = ET.ElementTree(root)
    return tree,root


tree,root = xml_to_string()

for studente in root.findall('studente'):
    nome = studente.find('nome')
    eta = studente.find('eta')
    print(f"Nome Studente: {nome.text}, età: {eta.text}")


tree.write('Corso Python/Martedì 9/file.xml')