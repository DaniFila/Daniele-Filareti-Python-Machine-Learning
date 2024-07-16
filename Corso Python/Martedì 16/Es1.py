import numpy as np

def punto_1():
    matr = np.random.randint(1,101,36)
    matr_s = matr.reshape(6,6)
    return matr_s


def punto_2(matr):
    matr_4x4 = matr[1:5,1:5]
    return matr_4x4


def punto_3(matr_4x4):
    in_matr = matr_4x4[::-1]
    return in_matr

def punto_4(in_matr):
    diag_princ = in_matr.diagonal()
    return diag_princ

def punto_5(in_matr):
    c_in_matr = in_matr
    c_in_matr[c_in_matr%3==0] = -1
    return c_in_matr


def main():
    matr = punto_1()
    print(f"Matrice originale:\n {matr}\n")
    matr_4x4 = punto_2(matr)
    print(f"Sotto matrice 4x4:\n {matr_4x4}\n")
    in_matr = punto_3(matr_4x4)
    print(f"Matrice invertita:\n {in_matr}\n")
    diag_princ = punto_4(in_matr)
    print(f"Diagonale principale:\n {diag_princ}\n")
    in_matr_5 = punto_5(in_matr)
    print(f"Matrice invertita modificata:\n {in_matr_5}\n")


main()

