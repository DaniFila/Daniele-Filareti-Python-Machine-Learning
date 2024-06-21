def verifica_primo(n):    # funzione per verifica un numero primo
    primo = True        # variabile locale per verifica primo
    for i in range(2,n-1):
        if n%i == 0:       # scan per identificare divisori di n
            primo = False
    if primo:
        return print("è un numero primo")    # la funzione restituisce una stampa in base al valore di primo
    else:
        return print("non è un numero primo")

def verifica_intero(a):    # funzione per verificare che la stringa digitata sia solo intero
    if not a.isdigit():
        return False    # restituisce valore booleano a seconda della condizione
    return True



N = input("Inserire un numero per la verifica: ")   # numero preso in input
while not verifica_intero(N):     # si verifica se il numero è inserito correttamente ed eventualmente si cicla richiamando la funzione 
    print("Errore")
    N = input("Inserire un numero per la verifica: ") 

verifica_primo(int(N))   # infine si richiama la funzione per la verifica primo
