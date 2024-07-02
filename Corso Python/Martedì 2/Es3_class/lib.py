class Libro:
    def __init__(self,titolo,autore,isbn):  # attributi dell'istanza
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self): # metodo che stampa la descizione dell'oggetto
        print(f"Il titolo del libro è: {self.titolo}, l'autore è: {self.autore},il codice isbn è: {self.isbn}")