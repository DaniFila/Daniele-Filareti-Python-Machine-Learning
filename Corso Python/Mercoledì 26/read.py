with open("Mercoledì 26/file.csv","r") as file:   # con il with andiamo a fare operazioni che me le chiuderà in automatico uscito dal with
    contenuto = file.read() # mi legge il file e me lo salva in una variabile del programma così da poterlo utilizzare quando chiudiamo il file


righe = contenuto.split("\n")  #mi salva ogni riga del file in lista e me li separa ad ogni a capo

print(righe)
elementi = []
for elemento in righe:
    elementi.append(elemento.split(","))  # questo mi inserire ogni riga in una lista dentro la lista
    print(elemento.split(",")[0]) # qui mi stampa solo l'indice 0 della prima parola delle righe separate da virgola



print(elementi)