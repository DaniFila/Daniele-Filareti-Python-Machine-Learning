import numpy as np

def punto_1(): # funzione che genera matrice con numeri randomici da tra 10 e 50 formando una 4x4
    a = np.random.randint(10,51,size=(4,4))
    print(f"\nMatrice generata:\n{a}")
    return a

def punto_2(a): # funzione che utilizza la tecnica del fancy indexing, salvando in una lista tutti gli indici dove farà un for e li stamperà
    indici = [[0,1],[1,3],[2,2],[3,0]]
    for indice in indici:
        print(f"\nElementi nell'indice: {indice} = \n{a[indice]}")

def punto_3(a): # funzione che utilizza la tecnica del fancy indexing per visualizzare le righe dispari
    indice = [1,3]
    print(f"\nrighe con indici dispari:\n{a[indice]}")

def punto_4(a): # funzione che utilizza la tecnica del fancy indexing e che a ogni elemento negli indici va a sommare uno scalare
    indici = [[0,1],[1,3],[2,2],[3,0]]
    for indice in indici:
        print(f"\nElementi nell'indice: {indice} = \n{a[indice]}")
        a[indice] = a[indice] + 10
        print(f"\nElementi modificati nell'indice: {indice} = \n{a[indice]}")

def menu(): # funzione menù con richiesta scelta all'utente
    info = """\n1: Fancy indexing
2: Fancy indexing righe dispari
3: Fancy indexing e somma 10 nell'indice
4: Exit
"""
    scelta_menu = input(info)
    return scelta_menu

def main(): # funzione main che richiama le altre funzioni
    matrice = punto_1()
    while True:
        scelta_menu = menu()
        if scelta_menu == "1":
            punto_2(matrice)
        elif scelta_menu == "2":
            punto_3(matrice)
        elif scelta_menu == "3":
            punto_4(matrice)
        elif scelta_menu =="4":
            break
        else:
            print("\nScelta non valida") 

main()   