class Libro:
    def __init__(self,autore,titolo,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def __str__(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} è ha {self.pagine} pagine."



libr = Libro("Dante Alighieri","La Divina Commedia",0)


print(libr)