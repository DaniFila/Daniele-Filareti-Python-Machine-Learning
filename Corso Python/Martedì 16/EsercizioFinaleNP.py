import numpy as np


def crea_matrice(): #creazione della matrice
    while True:     #inserimento righe e colonne con un while finchè non viene inserito un valore accettabile
        try:        
            righe=int(input("Inserisci il numero di righe: "))
            break
        except ValueError as e:
            print("\nErrore nel valore passato:", e, "\nInserisci un valore intero valido! \n")   #except con ValueError nel caso in cui si inserisce un valore non intero
    while True:
        try:
            col=int(input("Inserisci il numero di colonne: "))
            break
        except ValueError as e:
            print("\nErrore nel valore passato:", e, "\nInserisci un valore intero valido! \n")   #except con ValueError nel caso in cui si inserisce un valore non intero

    matrice = np.random.randint(0,100,size=(righe,col))
    print(f"\nLa matrice 2D di partenza è:\n {matrice}")

    return matrice,righe,col    #return della matrice creata, delle righe e delle colonne

def sotto_matrice(matrice,righe,col): #calcolo sottomatrice dalla prima riga alla penultima, e dalla prima colonna alla penultima
    print(f"\nSotto-Matrice centrale:\n {matrice[1:righe-1,1:col-1]}")    #sotto-matrice tramite Slicing

def trasp_matrice(matrice): #calcolo matrice trasposta
    trasposta=matrice.T     #metodo numpy per il calcolo della trasposta
    print("\nMatrice Trasposta: \n", trasposta)

def somma_elem(matrice): #somma degli elementi della matrice
    print(f"\nLa somma degli elementi della matrice è: {np.sum(matrice)}")

def det_mat(matrice,righe,col): #calcolo determinante della matrice se righe==col
    if righe==col:
        print(f"\nIl determinante della matrice è: {np.linalg.det(matrice)}") #calcolo determinante tramite linalg.det solo se righe e colonne sono uguali
    else:
        print("\nNumero di righe e colonne diverso. Non si può calcolare il determinante. ")

def molt_elem_wise(matrice,righe,col): #moltiplicazione element-wise
    matrice2=np.random.randint(0,100,size=(righe,col))
    prodotto_matrici=matrice*matrice2   #prodotto elemento per elemento
    print(f"\nSeconda matrice generata:\n{matrice2}\n")
    print(f"Prodotto delle due matrici:\n {prodotto_matrici}")

def media_mat(matrice): #calcolo media della matrice
    print(f"\nLa media degli elementi della matrice è: {np.mean(matrice)}")