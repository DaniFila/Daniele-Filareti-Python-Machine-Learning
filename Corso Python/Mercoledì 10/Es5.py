import requests
import json
from random import randint

def scrivi_file(dizionario):
    file_json= json.dumps(dizionario)
    with open("4 settimana\mercoledi 5\pokedex.json","w") as file:
        file.write(file_json)

def lettura_file():
    with open("4 settimana\mercoledi 5\pokedex.json", "r") as file:
        contenuto = file.read()

    dizionario_json = json.loads(contenuto)
    return dizionario_json

def verifica_file():
    try:
        pokedex=lettura_file()
    except:
        print("File non esistente. Creazione nuovo file")
        pokedex={}
        scrivi_file(pokedex)
        print("file creato")
    return pokedex

def pokemon_casuale():
    casuale=str(randint(1,20))
    risposta=requests.get(f"https://pokeapi.co/api/v2/pokemon/1")
    risposta_json=risposta.json()
    diz_temp={}
    exp=risposta_json["base_experience"]
    print(exp)
    nome=risposta_json["forms"][0]["name"]
    print(nome)
    id=risposta_json["id"]
    print(id)
    abilita=risposta_json["abilities"]
    peso=risposta_json["weight"]
    altezza=risposta_json["height"]

    return diz_temp

pokedex=verifica_file()
pokemon_casuale()