import numpy as np
def crea_array():
    a = np.random.randint(10,51, size=20) # creo array con numeri casuali nel range 10 e 50 di dimensione 20
    return a

def main():
    arr = crea_array() # richiamo la funzione per creare array
    print(f"Array di partenza: {arr}") # stampo array di partenza
    print(f"I primi 10 elementi dell'array: {arr[:10]}") # stampo i primi 10 elementi dell'array
    print(f"Gli ultimi 5 elementi dell'array: {arr[15:21]}") # stampo gli ultimi 5 elementi dell'array
    print(f"Elementi dall'indice 5 all'indici 15 escluso: {arr[5:15]}") # stampo gli elementi dall'indici 5 al 15 escluso
    print(f"Ogni terzo elemento dell'array: {arr[::3]}") # stampo ogni terzo elemento dell'array
    print("Cambio elementi con valore 99 dall'indice 5 al 10 escluso...")
    arr[5:10] = 99 # modifico il valore degli elementi dell'array nell'intervallo di indice 5 e 10 escluso
    print(f"Risultato: {arr}") # stampo l'array modificato



main()

def menù():
    info = "\n1: primi 10 elementi dell'array\n2: ultimi 5 elementi dell'array\n3:Elementi dall'indice 5 all'indici 15 escluso\n4: Ogni terzo elemento dell'array\n5: Cambio elementi con valore 99 dall'indice 5 al 10 escluso\n6: exit\n "
    scelta_menu = input(info)
    return scelta_menu