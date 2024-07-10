import xml.etree.ElementTree as ET
import pandas as pd



xml_content = """<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>
"""

root = ET.fromstring(xml_content)
colonne = ["titolo","autore"]
righe = []
for nodo in root:
    titolo = nodo.find("titolo").text
    autore = nodo.find("autore").text
    righe.append({"titolo":titolo,"autore":autore})

df = pd.DataFrame(righe,columns=colonne)

df.to_csv("Corso Python/Mercoledì 10/Es2.csv",index=False)
df.to_html("Corso Python/Mercoledì 10/Es2.html",index=False)