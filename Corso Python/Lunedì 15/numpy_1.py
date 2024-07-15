import numpy as np


arr = np.array([1,2,3,4,5])

arr2d = np.array([[1,2,3],[4,5,6]])

print("Forma dell'array:", arr.shape)  # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)  # Output: 1
print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size)  # Output: 5
print("Somma degli elementi:", arr.sum())  # Output: 15
print("Media degli elementi:", arr.mean())  # Output: 3.0
print("Valore massimo:", arr.max())  # Output: 5
print("Indice del valore massimo:", arr.argmax())  # Output: 4


#------------------------------------------------------------------------------------------

arr1 = np.array([1,2,3,4],dtype = 'int32')


print("Il tipo dell'array arr2 è:",arr1.dtype)



arrp = np.arange(6)

print(arrp)

reshaped_arrp = arrp.reshape(2, 3)

print(reshaped_arrp)