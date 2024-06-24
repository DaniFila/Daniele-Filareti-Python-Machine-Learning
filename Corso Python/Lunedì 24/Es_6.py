dizionario = {}
verifica_pari = True
n = input("Inserire un numero: ")
while not n.isnumeric():
    print("Inserire valore numerico")
    n = input("Inserire un numero: ")


if int(n)%2 != 0:
    verifica_pari = False



dizionario["quadrato"] = int(n)*2
dizionario["pari"] = verifica_pari
dizionario["cifre"] = len(n)

print(dizionario)