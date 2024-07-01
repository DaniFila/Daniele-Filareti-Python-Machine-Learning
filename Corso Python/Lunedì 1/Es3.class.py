class Libro:
    def __init__(self,autore,titolo,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} è ha {self.pagine} pagine."


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
            
    


libr = Biblioteca.crea_libro()







            


