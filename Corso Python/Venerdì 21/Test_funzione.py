def verifica_primo(n):
    primo = True
    for i in range(2,n-1):
        if n%i == 0:
            primo = False
    if primo:
        return print("è un numero primo")
    else:
        return print("non è un numero primo")

def verifica_intero(a):
    if not a.isdigit():
        return False
    return True



N = input("Inserire un numero per la verifica: ")
while not verifica_intero(N):
    print("Errore")
    N = input("Inserire un numero per la verifica: ")

verifica_primo(int(N))
