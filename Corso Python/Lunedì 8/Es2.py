import numpy as np

arr_equidistanti = np.linspace(0,1,12)

arr_equidistanti_matr= arr_equidistanti.reshape(3,4)

matr_random = np.random.rand(3,4)


print(f"La somma della prima matrice è: {np.sum(arr_equidistanti_matr)}\nLa somma della seconda matrice è: {np.sum(matr_random)}")