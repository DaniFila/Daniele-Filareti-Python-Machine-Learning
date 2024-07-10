import requests
import xml.etree.ElementTree as ET

contenuto = requests.get("https://www.ansa.it/sito/ansait_rss.xml")

xml_contenuto = contenuto.text
root = ET.fromstring(xml_contenuto)

prima_notizia = root.find("channel/item")


titolo = prima_notizia.find("title").text
link = prima_notizia.find("link").text
descrizione = prima_notizia.find("description").text
pub_date = prima_notizia.find("pubDate").text

print(f"Titolo: {titolo}")
print(f"Link: {link}")
print(f"Descrizione: {descrizione}")
print(f"Data pubblicazione: {pub_date}")
    

tree = ET.ElementTree(root)

tree.write("Corso Python/Mercoledì 10/Es1.xml")