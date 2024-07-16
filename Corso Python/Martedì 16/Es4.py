import numpy as np

def crea_array(): # creo array con elementi casuali tra 1 e 100 con 15 elementi
    a = np.random.randint(1,101,15)
    return a 

def somma(a): # effettuo la somma degli elementi nell'array passato in funzione
    s = np.sum(a)
    return s
def media(a): # effettuo la media degli elementi nell'array passato in funzione
    m = np.mean(a)
    return m

def main(): # funzione main che richiama le 3 funzioni e stampa i risultati
    array = crea_array()
    somma_e_array = somma(array)
    media_e_array = media(array)
    print(f"Array causale:\n{array}")
    print(f"Somma elementi array:\n{somma_e_array}")
    print(f"Media elementi array:\n{media_e_array}")

main()