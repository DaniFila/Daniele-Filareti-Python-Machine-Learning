import numpy as np

def crea_array(): # creo array con elementi casuali tra 1 e 100 con 15 elementi
    a = np.random.randint(1,101,15)
    print(f"\nArray causale:\n{a}")
    return a 

def somma(a): # effettuo la somma degli elementi nell'array passato in funzione
    s = np.sum(a)
    print(f"\nSomma elementi array:\n{s}")

def media(a): # effettuo la media degli elementi nell'array passato in funzione
    m = np.mean(a)
    print(f"\nMedia elementi array:\n{m}")

def main(): # funzione main che richiama le 3 funzioni e stampa i risultati
    array = crea_array()
    while True:
        scelta_menu = menu()
        if scelta_menu == "1":
            somma(array)
        elif scelta_menu == "2":
            media(array)
        elif scelta_menu == "3":
            break
        else:
            print("\nScelta non valida!")

def menu(): # funzione menù che stampa un menù e richiede da input la scelta
    info = """1: Calcola e stampa la somma
2: Calcola e stampa la media
3: Exit
"""
    scelta_menu = input(info)
    return scelta_menu


main()