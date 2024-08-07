import numpy as np
# Esercizio 1

arr = np.full(10,5) # creato array di 10 elementi uguali a 5

arr_matr = arr.reshape(2,5) # dall'array si crea una matrice

matr_casuale = np.random.rand(4,4) # matrice casuale 4x4 con numeri tra 0 e 1

#--------------------------------------------------------------------------------------------
# Esercizio 2

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # matrice 1 3x3

arr2 = np.array([[1,2,5],[46,5,6],[7,8,10]]) # matrice 2 3x3

for i in range(3):
    for j in range(3):
        prodotto = arr1[i][j]*arr2[i][j] # prodotto delle 2 matrici elemento per elemento
        # print(prodotto)


arr3 = np.linspace((1,9),3,3)

somma = np.sum(arr3)

#--------------------------------------------------------------------------------------------
# Esercizio 3

def crea_array_equi(): # creo una funzione che genera un array con 20 numeri equidistanti da 0 a 10
    arr = np.linspace(0,10,20)
    return arr

def matr_random(): # creo una funzione che genera una matrice di dimensione 5x5 con numeri casuali da 1 a 100
    arr = np.random.randint(1,101, size=(5,5))
    return arr


#---------------------------------------------------------------------------------------------------------------------------------

# Esercizio 4

arr_0 = np.random.rand(5,5) # matrice 5x5 con numeri casuali


media = np.mean(arr_0,axis=0) # si calcola la media con la funzione mean indicando axis = 0 per indicare la media delle colonne

somma = np.sum(arr_0,axis=1) #  si calcola la somma di ciascuna riga della matrice con la funzione sum con axis = 1 per indicare le righe

#---------------------------------------------------------------------------------------------------------------------------------

# Esercizio 5

arr1d = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # creo un array con 12 elementi

matr_arr1d = arr1d.reshape(3,4) # lo trasformo in una matrice 3x4

matr_arr1d[:,0] = 0 # trasformo la prima colonna in 0, posso usare 2 metodi
#for i in range(3):
   # matr_arr1d[i][0] = 0


#---------------------------------------------------------------------------------------------------------------------------------

# Esercizio 6

matrice_casuale = np.random.randint(50, 101, size=(3, 3)) # matrice con numeri casuali 3x3

valore_massimo = np.max(matrice_casuale) # mi salvo in una variabile il valore massimo della matrice attraverso la funzione max
valore_minimo = np.min(matrice_casuale) # mi salvo in un'altra variabile il valore minimo della matrice attraverso la funzione min


array1 = np.random.rand(5) # genero 2 array con numeri casuali di dimensione 5
array2 = np.random.rand(5)

prodotto_scalare = np.dot(array1, array2) # faccio il prodotto scalare attraverso la funzione dot dei 2 array generati casualmente
