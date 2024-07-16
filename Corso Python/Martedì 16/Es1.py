import numpy as np

def punto_1():
    matr = np.random.randint(1,101,36)
    matr_s = matr.reshape(6,6)
    return matr_s


def punto_2(matr):
    matr_4x4 = matr[1:5,1:5]
    return matr_4x4


def punto_3(matr_4x4):
    in_matr = matr_4x4[::-1,::]
    return in_matr


matr = punto_1()
matr_4x4 = punto_2(matr)
in_matr = punto_3(matr_4x4)

print(matr_4x4)
print(in_matr)