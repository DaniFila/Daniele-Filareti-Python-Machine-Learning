lista = []

while True:
    a = input("Inserire parola (0 per terminare): ")
    if a == "0":
        break
    else:
        lista.append(a)
    


for i in lista:
    print("La lunghezza della parola",i,"è",len(i)
          )