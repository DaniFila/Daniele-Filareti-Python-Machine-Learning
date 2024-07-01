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
            contenuto = input("contenuto")
            self.paginel.append(Pagina(i,contenuto))

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
    
    


libr = Biblioteca.crea_libro()







            


