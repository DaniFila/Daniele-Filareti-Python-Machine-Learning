# FILTER, MAP
numeri = [1,2,3,4,5,6,7,8,9,10]
def numeri_pari(a):
    return a%2 == 0


lista_numeri_pari = list(filter(numeri_pari,numeri)) # Filtra eseguendo una funzione su tutti gli elementi di un iterabile

print(lista_numeri_pari)

lista_controllo_se_pari_o_dispari = list(map(numeri_pari,numeri)) # esegue una funzione su tutti gli elementi di un iterabile


print(lista_controllo_se_pari_o_dispari)