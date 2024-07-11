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
    for chiave in pokedex:
        id = chiave
        print(f"ID: {id} nome: {pokedex[id]["nome"]},exp: {pokedex[id]["exp"]}, abilità: {pokedex[id]["abilità"]}, peso: {pokedex[id]["peso"]}, altezza: {pokedex[id]["altezza"]}")
    










pokedex = verifica_file()
pokemon, id = pokemon_casuale()
#aggiornamento_pokedex(pokemon,pokedex,id)
visualizza_pokedex(pokedex)