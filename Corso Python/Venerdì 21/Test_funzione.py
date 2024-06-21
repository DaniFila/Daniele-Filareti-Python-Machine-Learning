def verifica_primo(n):
    primo = True
    for i in range(2,n-1):
        if n%i == 0:
            primo = False
    return primo




N = int(input("Inserire un numero per la verifica: "))

if verifica_primo(N):
    print("é un numero primo")
else:
    print("non è un numero primo")    