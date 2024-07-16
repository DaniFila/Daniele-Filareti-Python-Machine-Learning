import numpy as np

def crea_matrice(): # funzione che crea matrice 5x5 con valori contigui da 1 a 25
    a = np.linspace(1,25,25)
    a_matr = a.reshape(5,5)
    print(f"Matrice generata:\n{a_matr}")
    return a_matr

def stampa_seconda_colonna(a): # funzione che stampa la seconda colonna
    print(f"Seconda colonna matrice:\n{a[::,1:2]}")

def stampa_terza_riga_matrice(a): # funzione che stampa la terza riga
    print(f"Terza riga matrice:\n{a[2:3]}")

def somma_diagonale_principale(a): # funzione che stampa la diagonale principale e restituisce la somma
    diagonale = a.diagonal()
    somma = np.sum(diagonale)
    print(f"La diagonale principale è:\n{diagonale} la somma è: {somma}")

def main(): # funzione main che richiama tutte le funzioni
    matrice = crea_matrice()
    while True:
        scelta_menu = menu()
        if scelta_menu == "1":
            stampa_seconda_colonna(matrice)
        elif scelta_menu == "2":
            stampa_terza_riga_matrice(matrice)
        elif scelta_menu == "3":
            somma_diagonale_principale(matrice)
        elif scelta_menu == "4":
            break
        else:
            print("Scelta non valida")

def menu(): # funzione menu per stampare il menù e chiedere in input la scelta
    info = """1: Visualizza seconda colonna
2: Visualizza terza riga
3: Visualizza diagonale principale e stampa la somma dei suoi elementi
4: Exit
"""
    scelta_menu = input(info)
    return scelta_menu

main()


