import requests
import xml.etree.ElementTree as ET
import pandas as pd

contenuto = requests.get("https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml").text

root = ET.fromstring(contenuto)


colonne = ["titolo","link","descrizione","data di pubblicazione"]
righe = []

for nodo in root.findall("channel/item"):
    titolo = nodo.find("title").text
    link = nodo.find("link").text
    descrizione = nodo.find("description").text
    pub_date = nodo.find("pubDate").text
    righe.append({"titolo":titolo,"link":link,"descrizione":descrizione,"data di pubblicazione":pub_date})

df = pd.DataFrame(righe,columns=colonne)

df.to_csv("Corso Python/Mercoledì 10/Es3.csv",index=False)
df.to_html("Corso Python/Mercoledì 10/Es3.html",index=False)




