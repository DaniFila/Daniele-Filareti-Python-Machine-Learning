import numpy as np

def punto_1(): # funzione che crea array con 50 elementi equidistanti da 0 a 10
    a = np.linspace(0,10,50)
    return a

def punto_2(): # funzione che crea array con valori casuali tra 0 e 1 con 50 elementi
    a = np.random.rand(50)
    return a

def punto_3(arr1,arr2): # funzione che crea array sommando elemento per elemento dai 2 array
    try:
        a = np.add(arr1,arr2)
        return a
    except:
        print("Argomenti passati non validi per effettuare operazione!")

def punto_4(arr): # funzione che calcola la somma di un array
    try:
        somma = np.sum(arr)
        return somma
    except:
        print("Argomento passato non valido per effettuare operazione!")

def punto_5(arr): # funzione che calcola la somma di un array con la condizione che l'elemento deve essere maggiore di 5
    try:
        somma = np.sum(arr[arr>5])
        return somma
    except:
        print("Argomento passato non valido per effettuare operazione!")

def punto_7(arr_equi,arr_random,sum_arr,sum_elem,sum_cond): # funzione che stampa tutte le operazioni delle altre funzioni
    print(f"\nArray con 50 elementi equidistanti da 0 a 10:\n{arr_equi}")
    print(f"\nArray con 50 elementi casuali tra 0 e 1:\n{arr_random}")
    print(f"\nArray somma dei 2 array:\n{sum_arr}")
    print(f"\nSomma elementi dell'array:\n{sum_elem}")
    print(f"\nSomma elementi dell'array maggiori di 5:\n{sum_cond}")


def menu(): # funzione che crea un menu e l'interazione da input della scelta
    info = """\n1: Visualizza Array con elementi equidistanti da 0 a 10
2: Visualizza Array con elementi randomici tra 0 e 1
3: Visualizza Array della somma dei 2 array
4: Effettuare somma elementi Array generato dalla somma degli elementi dei 2 array
5: Effettuare somma elementi Array generato dalla somma degli elementi dei 2 array con condizione elemento maggiore di 5
6: Visualizzare operazioni di tutte le funzioni
7: Exit
"""
    scelta_menu = input(info)
    return scelta_menu


def main(): # funzione main che richiama tutte le funzioni ed effettua le operazioni scelte da input
    arr_equi = punto_1()
    arr_random = punto_2()
    sum_arr = punto_3(arr_equi,arr_random)
    sum_elem = punto_4(sum_arr)
    sum_cond = punto_5(sum_arr)
    if sum_arr != None:
        while True:
            scelta_menu = menu()
            if scelta_menu == "1":
                print(f"\nArray con 50 elementi equidistanti da 0 a 10:\n{arr_equi}")
            elif scelta_menu == "2":
                print(f"\nArray con 50 elementi casuali tra 0 e 1:\n{arr_random}")
            elif scelta_menu == "3":
                print(f"\nArray somma dei 2 array:\n{sum_arr}")
            elif scelta_menu == "4":
                print(f"\nSomma elementi dell'array:\n{sum_elem}")
            elif scelta_menu == "5":
                print(f"\nSomma elementi dell'array maggiori di 5:\n{sum_cond}")
            elif scelta_menu == "6":
                punto_7(arr_equi,arr_random,sum_arr,sum_elem,sum_cond)
            elif scelta_menu == "7":
                break
            else:
                print("Scelta non valida")
    else:
        print("Non è possibile proseguire!")


main()