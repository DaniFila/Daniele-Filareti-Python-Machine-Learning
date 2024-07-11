import requests
import json
from random import randint

def scrivi_file(dizionario):
    file_json= json.dumps(dizionario)
    with open("Corso Python/Mercoledì 10/Es5.json","w") as file:
        file.write(file_json)

def lettura_file():
    with open("Corso Python/Mercoledì 10/Es5.json", "r") as file:
        contenuto = file.read()

    dizionario_json = json.loads(contenuto)
    return dizionario_json

def verifica_file():
    vuoto = False
    try:
        pokedex=lettura_file()
    except:
        print("File non esistente. Creazione nuovo file")
        vuoto = True
        print("file creato")
    return pokedex,vuoto

def pokemon_casuale():
    casuale=str(randint(1,20))
    risposta=requests.get(f"https://pokeapi.co/api/v2/pokemon/{casuale}")
    api_poke_casuale=risposta.json()
    pokemon={}
    exp=api_poke_casuale["base_experience"]
    nome=api_poke_casuale["forms"][0]["name"]
    id=api_poke_casuale["id"]
    abilita=api_poke_casuale["abilities"]
    peso=api_poke_casuale["weight"]
    altezza=api_poke_casuale["height"]
    pokemon = {"nome":nome,"exp":exp,"abilità":abilita,"peso":peso,"altezza":altezza}
    print("\nID:",id,"nome:", pokemon["nome"], "exp:", pokemon["exp"], "peso:", pokemon["peso"], "altezza:", pokemon["altezza"])

    
    return pokemon,id

def aggiornamento_pokedex(pokemon,pokedex,id):
    trovato = False
    for idp in pokedex:
        if idp == id:
            trovato = True
            print("Il pokemon si trova già nel pokedex")
    if not trovato:
        print("Il pokemon non si trova nel pokedex,aggiunta in corso...")
        pokedex[id] = pokemon
        print("Pokemon aggiunto!")
        scrivi_file(pokedex)

def visualizza_pokedex(pokedex):
    if vuoto:
        print("Il pokedex è vuoto")
    else:
        lista_id = []
        for chiave in pokedex:
            lista_id.append(chiave)
        for id in lista_id:
            abilità = pokedex[id]["abilità"]
            print("ID:",id,"nome:", pokedex[id]["nome"], "exp:", pokedex[id]["exp"], "peso:", pokedex[id]["peso"], "altezza:", pokedex[id]["altezza"])
            print("Abilità:")
            for i in range(len(abilità)):
                print(abilità[i]["ability"]["name"])
            print("")

def menu():
    info_menu = "1: Visualizza Pokedex\n2: Genera pokemon casuale\n0: Exit\n"
    scelta_menu = input(info_menu)
    return scelta_menu


while True:
    pokedex,vuoto = verifica_file()
    scelta_menù = menu()
    if scelta_menù == "1":
        visualizza_pokedex(pokedex)
    elif scelta_menù == "2":
        pokemon,id = pokemon_casuale()
        scelta = input("Vuoi salvarlo? 1 per confermare: ")
        if scelta == "1":
            aggiornamento_pokedex(pokemon,pokedex,id)
        else:
            print("Arrivederci!")
    elif scelta_menù == "0":
        break
    else:
        print("Error")