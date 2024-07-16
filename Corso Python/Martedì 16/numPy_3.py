import numpy as np

A = np.array([[1,2],[3,4]]) # creazione di una matrice quadrata

A_inv = np.linalg.inv(A) # calcolo dell'inversa della matrice

print(A,"\n",A_inv)