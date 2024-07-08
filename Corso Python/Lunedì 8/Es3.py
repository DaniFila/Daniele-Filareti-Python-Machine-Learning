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

def crea_array_equi():
    n = int(input("Indicare numero di elementi: "))
    inizio = int(input("Indicare estremo sinistro: "))
    fine = int(input("indicare estremo destro: "))
    arr = np.linspace(inizio,fine,n)
    return arr

def matr_random():
    arr = np.random.randint(1,101, size=(5,5))
    return arr


#----------------------------------------------------------------------------------------------

# Esercizio 4





