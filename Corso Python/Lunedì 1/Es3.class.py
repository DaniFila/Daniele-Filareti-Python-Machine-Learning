class Libro:
    def __init__(self,autore,titolo,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.paginel = []

    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} è ha {self.pagine} pagine."

    def crea_pagine(self):
        for i in range(1,self.pagine+1):
            contenuto = input("Indicare contenuto pagina: ")
            self.paginel.append(Pagina(i,contenuto))

    def stampa_pagine(self):
        for i in range(len(self.paginel)):
            print(self.paginel[i])


class Biblioteca:
    def crea_libro():
        libri =[]
        while True:
            titolo = input("Inserire titolo: ")
            autore = input("Inserire autore: ")
            pagine = input("Inserire pagine: ")
            libri.append(Libro(titolo,autore,pagine))
            a = input("Vuoi aggiungere un nuovo libro (si per continuare)? ")
            if a != "si":
                break 
        return libri
            


class Pagina:
    def __init__(self,numero,contenuto):
        self.numero = numero
        self.contenuto = contenuto
    
    def __str__(self):
        return f"Pagina {self.numero}: {self.contenuto}"
    

libr1 = Libro("boh","sapim",2)

libr1.crea_pagine()

libr1.stampa_pagine()



# libr = Biblioteca.crea_libro()







            


