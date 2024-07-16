import numpy as np

def punto_1():
    matr = np.random.randint(1,101,36) # creo array con 36 elementi casuali tra 1 e 100
    matr_s = matr.reshape(6,6) # riformatto l'array in matrice 6x6
    return matr_s

def punto_2(matr):
    matr_4x4 = matr[1:5,1:5] # estraggo la matrice centrale da quella 6x6 in una matrice 4x4 utilizzando lo slicing di righe e colonne
    return matr_4x4

def punto_3(matr_4x4):
    in_matr = matr_4x4[::-1] # inverto le righe di posizione
    return in_matr

def punto_4(in_matr):
    diag_princ = in_matr.diagonal() # estraggo la matrice diagonale principale da quella invertita
    return diag_princ

def punto_5(in_matr):
    in_matr[in_matr%3==0] = -1 # modifico tutti i valori che sono multipli per 3 e li cambio con -1
    return in_matr

def punto_6(matr,matr_4x4,in_matr,diag_princ,in_matr_5): # funzione che richiama tutte le funzioni e stampa i vari risultati
    print(f"Matrice originale:\n {matr}\n")
    print(f"Sotto matrice 4x4:\n {matr_4x4}\n")
    print(f"Matrice invertita:\n {in_matr}\n")
    print(f"Diagonale principale:\n {diag_princ}\n")
    print(f"Matrice invertita modificata:\n {in_matr_5}\n")

def menu():
    info = """1: crea sotto matrice
2: inverti righe matrice
3: estrai diagonale principale
4: modifica matrice invertita
5: stampa tutte le funzioni
6: exit
"""
    scelta_menu = input(info)
    return scelta_menu

def main():
    matr = punto_1()
    matr_4x4 = punto_2(matr)
    in_matr = punto_3(matr_4x4)
    diag_princ = punto_4(in_matr)
    in_matr_5 = punto_5(in_matr)
    while True:
        scelta_menu = menu()
        if scelta_menu == "1":
            print(f"Sotto matrice 4x4:\n {matr_4x4}\n")
        elif scelta_menu == "2":
            print(f"Matrice invertita:\n {in_matr}\n")
        elif scelta_menu == "3":
            print(f"Diagonale principale:\n {diag_princ}\n")
        elif scelta_menu == "4":
            print(f"Matrice invertita modificata:\n {in_matr_5}\n")
        elif scelta_menu == "5":
            punto_6(matr,matr_4x4,in_matr,diag_princ,in_matr_5)
        elif scelta_menu == "6":
            break
        else:
            print("Scelta non valida")

main()

