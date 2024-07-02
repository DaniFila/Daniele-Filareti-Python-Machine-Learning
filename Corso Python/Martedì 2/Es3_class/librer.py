import lib
class Libreria:
    catalogo =[]
    def aggiungi_libro(self): # attributi dell'istanza
        titolo = input("Inserire titolo: ")
        autore = input("Inserire autore: ")
        isbn = input("Inserisci codice isbn: ")
        self.catalogo.append(lib.Libro(titolo,autore,isbn))
    def rimuovi_libro(self): # metodo per rimuovere libro
        p = False # booleano per tracciare se il libro è stato trovato
        isbn = input("Indicare isbn del libro da eliminare: ") 
        for i in self.catalogo:
            if i.isbn == isbn: # si sfoglia tutto il catalogo e se l'isbn corrisponde si rimuove dalla lista
                    self.catalogo.remove(i)
                    print("Libro eliminato con successo!")
                    p = True
        if not p: # stampa se non si è trovata corrispondenza
              print("Libro non trovato.")
    def cerca_titolo(self): # metodo per cercare titolo
        search = [] # lista per aggiungere titoli trovati
        titolo = input("Indicare titolo del libro: ") 
        for i in self.catalogo:
            if titolo == i.titolo: # si sfoglia il catalogo e se si trova un titolo corrispondente si aggiunge alla lista
                 search.append(i)
        if search == []: # se la lista è vuota si stampa il messaggio di nessuna corrispondenza
            print("Nessun titolo trovato.")
        else:
            for i in search: # si sfoglia la lista e si stampa la descrizione del libro attraverso il metodo descrizione
                i.descrizione()
    def mostra_catalogo(self): # metodo per mostrare il catalogo
        for i in self.catalogo:
            i.descrizione() # si sfoglia e si richiama il metodo descrizione di ogni libro

        