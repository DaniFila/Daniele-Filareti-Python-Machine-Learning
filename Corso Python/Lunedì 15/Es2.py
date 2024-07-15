import numpy as np
def crea_array():
    a = np.random.randint(10,51, size=20) # creo array con numeri casuali nel range 10 e 50 di dimensione 20
    return a

def main():
    while True:
        arr = crea_array() # richiamo la funzione per creare array 
        a = f"Array: {arr}" # stampo array 
        b = f"I primi 10 elementi dell'array: {arr[:10]}" # stampo i primi 10 elementi dell'array
        c = f"Gli ultimi 5 elementi dell'array: {arr[15:21]}" # stampo gli ultimi 5 elementi dell'array
        d = f"Elementi dall'indice 5 all'indici 15 escluso: {arr[5:15]}" # stampo gli elementi dall'indici 5 al 15 escluso
        e = f"Ogni terzo elemento dell'array: {arr[::3]}" # stampo ogni terzo elemento dell'array
        f = arr[5:10] = 99 # modifico il valore degli elementi dell'array nell'intervallo di indice 5 e 10 escluso
        arr = crea_array() # richiamo la funzione per creare array 
        diz = {"1":b,"2":c,"3":d,"4":e,"5":f}
        scelta_menu = menù()
        print(diz[scelta_menu])
        print(f"Array intero: {arr}")
        z = input("Vuoi ripetere?")
        if z != "si":
            break
        
def menù():
    info = "\n1: primi 10 elementi dell'array\n2: ultimi 5 elementi dell'array\n3:Elementi dall'indice 5 all'indici 15 escluso\n4: Ogni terzo elemento dell'array\n5: Cambio elementi con valore 99 dall'indice 5 al 10 escluso\n "
    scelta_menu = input(info)
    return scelta_menu

main()
