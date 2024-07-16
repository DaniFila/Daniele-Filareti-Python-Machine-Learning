import numpy as np

def crea_matrice():
    while True:
        try:
            righe=int(input("Inserisci il numero di righe: "))
            break
        except:
            print("Errore. Riprova")
    while True:
        try:
            col=int(input("Inserisci il numero di colonne: "))
            break
        except:
            print("Errore. Riprova")

    matrice = np.random.randint(0,100,size=(righe,col))
    print(matrice)
    return matrice,righe,col

def sotto_matrice(matrice,righe,col):
    print(f"Sotto matrice centrale:\n {matrice[1:righe-1,1:col-1]}")

def trasp_matrice(matrice):
    matr=matrice.T
    print(matr)

def somma_elem(matrice):
    print(f"La somma della matrice è: {np.sum(matrice)}")

def det_mat(matrice,righe,col):
    if righe==col:
        print(f"Il determinante è: {np.linalg.det(matrice)}")
    else:
        print("Righe e colonne diverse. Non si può calcolare il determinante")

def molt_elem_wise(mat,righe,col):
    mat2=np.random.randint(0,100,size=(righe,col))
    molt=mat*mat2
    print(f"Seconda matrice generata:\n{mat2}")
    print(f"Moltiplicazione delle due matrici:\n {molt}")

def media_mat(matrice):
    print(f"La media della matrice è: {np.mean(matrice)}")