import random

def num_casuale():
    z = random.randint(1,100)
    print("Il numero casuale è:",z)
    return z


def input_num():
    n = input("Indovinare numero: ")
    return n

def verifica_intero(a):    # funzione per verificare che la stringa digitata sia solo intero
    if not a.isdigit():
        return False    # restituisce valore booleano a seconda della condizione
    return True

def gioco(a,b):
    if a == b:
        print("Hai vinto")
    else:
        print("non hai vinto")    

def main():
    n = input_num()
    while not verifica_intero(n):
        n = input_num()
    a = num_casuale()
    gioco(n,a)


main()