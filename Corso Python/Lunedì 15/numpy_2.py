import numpy as np

arr = np.array([1,2,3,4,5])
# Indexing
print(arr[0]) # stampa l'indice 0 dell'array
# Slicing
print(arr[1:3]) # stampa dall'indice 1 all'indice 3 escluso
# Boolean Indexing
print(arr[arr>2]) # stampa i numeri che sono maggiori di 2
print()
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# Slicing sulle righe
print(arr_2d[1:3]) # stampa solo la seconda e terza riga
# Slicing sulle colonne
print(arr_2d[:,1:3]) # stampa di tutte le righe solo la seconda e terza colonna
# Slicing misto
print(arr_2d[1:,1:3]) # stampa dalla seconda riga solo la seconda e terza colonna

