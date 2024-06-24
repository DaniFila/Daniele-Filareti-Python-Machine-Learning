


n1 = int(input("inserire primo numero: "))
n2 = int(input("inserire secondo numero: "))

print("SOMMA 1:")
print("SOTTRAZIONE 2:")
print("MOLTIPLICAZIONE 3:")
print("DIVISIONE 4:")
print("RESTO DIVISIONE 5:")
print("POTENZA 6:")
print("(altro per chiudere)")
print("")

z = input("Indicare scelta: ")

if z == "1":
    print("La somma è:", n1+n2)
elif z == "2":
    print("La sottrazione è:", n1-n2)
elif z == "3":
    print("La moltiplicazione è:", n1*n2)
elif z == "4":
    print("La divisione è:", n1/n2)
elif z == "5":
    print("La potenza è:", n1**n2)
   