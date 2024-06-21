import random   # libreria random per i numeri casuali

def num_casuale():  # funzione che restituisce un numero casuale e stampa qual è il numero casuale
    z = random.randint(1,100)
    print("Il numero casuale è:",z)   
    return z


def input_num():  # funzione che richiede in input un intero
    n = input("Indovinare numero: ")
    return n

def verifica_intero(a):    # funzione per verificare che la stringa digitata sia solo intero
    if not a.isdigit():
        return False    # restituisce valore booleano a seconda della condizione
    return True

def gioco(a,b):   # funzione che confronta 2 numeri e stampa in base al confronto
    if a == b:
        print("Hai vinto")
    else:
        print("non hai vinto")    

def main():  # funzione main contenente il richiamo di tutte queste funzioni
    n = input_num()
    while not verifica_intero(n):
        n = input_num()
    a = num_casuale()
    gioco(n,a)


main()    # richiamo della funzione main