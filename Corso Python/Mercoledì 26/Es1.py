from random import randint    

def read_file():     # Funzione che legge il file e salva il contenuto in una variabile
    with open("Mercoledì 26/Es1.csv","r") as f:     
        file = f.read()
    return file
        

    
        
def numeri_random_in_lista():  # funzione che genera numeri casuali inserendoli in una lista e li aggiunge in una stringa separati da virgola
    l = []
    while True:
        a = str(randint(0,21))
        if a not in l:
            l.append(a)
        if len(l) == 5:
            break
    sep = ","
    lista_in_stringa = sep.join(l)
    return lista_in_stringa   

l_string = numeri_random_in_lista()

  

with open("Mercoledì 26/Es1.csv", "w") as file: # si scrive nel file la stringa con numeri casuali
    file.write(l_string)

   

c = 0 # count di quanti indovinati
z = read_file()  # si salva il contenuto del file su z

str_file_in_lista = z.split(",")   # si converte in lista separando numeri con virgola

for i in range(5):
    a = input("prova a indovinare (numero da 0 a 20): ")  # si prendono i 5 numeri e si verificano
    for i in str_file_in_lista:
        if i == a:
            c+=1
            print("Hai indovinato",c,"numero/i")
            str_file_in_lista.pop(str_file_in_lista.index(i))
            
    

if c>=2:
    print("Hai vinto")  
else:
    print("Hai perso")    
