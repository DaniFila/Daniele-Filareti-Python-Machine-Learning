import numpy as np



while True:
    a = int(input("Indicare estremo sinistro: ")) # si indica estremo sinistro
    b = int(input("Indicare estremo destro (escluso): ")) # si indica estremo destro non incluso
    arr = np.arange(a,b) # si crea l'array nel range
    print("Il tipo di dato dell'array è:",arr.dtype) # si stampa il tipo di dato
    arr = arr.astype('float64') # si modifica il tipo in float64
    print("Il tipo di dato modificato è:",arr.dtype) # si stampa il tipo di dato modificato
    print("L'array è:",arr)  # si stampa l'array
    z = input("Vuoi ripetere? ") # si richiede se si vuole ripetere
    if z != "si":
        break

