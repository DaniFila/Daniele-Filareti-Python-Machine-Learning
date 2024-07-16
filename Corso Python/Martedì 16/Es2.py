import numpy as np



def crea_arr_equi():
    arr_equi = np.linspace(0,1,12)
    return arr_equi
def trasfroma_arr_in_matr(arr_equi):
    matr_arr_equi = arr_equi.reshape(3,4)
    return matr_arr_equi
def crea_matr_random():
    matr_random = np.random.rand(3,4)
    return matr_random


def somma(matr):
    sum = np.sum(matr)
    return sum

def main():
    arr_equi = crea_arr_equi()
    matr_arr_equi = trasfroma_arr_in_matr(arr_equi)
    matr_random = crea_matr_random()
    somma_matr_arr_equi = somma(matr_arr_equi)
    somma_matr_random = somma(matr_random)
    print(f"La somma elementi della matrice 3x4 con numeri equidistanti tra 0 e 1:\n {somma_matr_arr_equi}")
    print(f"Somma elementi matrice random:\n {somma_matr_random}")


main()