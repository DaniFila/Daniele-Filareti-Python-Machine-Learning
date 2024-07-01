class Libro:
    def __init__(self,autore,titolo,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} è ha {self.pagine} pagine."


class Biblioteca:
    def crea_libro():
        titolo = input("Inserire titolo: ")
        autore = input("Inserire autore: ")
        pagine = input("Inserire pagine: ")
        return Libro(titolo,autore,pagine)
    


libr = Biblioteca.crea_libro()


print(libr)




            


