import numpy as np
# Inversa di una matrice
A = np.array([[1,2],[3,4]]) # creazione di una matrice quadrata

A_inv = np.linalg.inv(A) # calcolo dell'inversa della matrice

print(A,"\n",A_inv)



# Norma di un vettore

v = np.array([3,4])

# calcolo della norma del vettore

norm_v = np.linalg.norm(v)

print(norm_v)