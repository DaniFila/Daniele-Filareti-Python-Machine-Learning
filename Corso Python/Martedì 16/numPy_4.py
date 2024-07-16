import numpy as np

arr = np.array([1,2,3,4])
scalar = 10

# Brodcasting aggiunge lo scalare a ogni elemento dell'array

result = arr + scalar

print(result)


#--------------------------------------

# creazione array
a = np.array([1,2,3])
b = np.array([4,5,6])

# operazioni aritmetiche
c = a + b 

# funzioni matematiche
d = np.sin(a)

# Algebra lineare
e = np.dot(a,b) # prodotto scalare

#Broadcasting
f = a + 10

print(a,b,c,d,e,f,sep="\n")

