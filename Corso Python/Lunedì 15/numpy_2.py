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


#----------------------------

arr1 = np.array([0,1,2,3,4,5,6,7,8,9])

# Slicing di base
print(arr1[2:7])  # Output: [2 3 4 5 6]

# Slicing con passo
print(arr1[1:8:2])  # Output: [1 3 5 7]

# Omettere start e stop
print(arr1[:5])  # Output: [0 1 2 3 4]
print(arr1[5:])  # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:])  # Output: [5 6 7 8 9]
print(arr[:-5])  # Output: [0 1 2 3 4]