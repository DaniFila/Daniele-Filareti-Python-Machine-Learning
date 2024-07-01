class Ristorante:  
    menu = {}    
    apertura = False
    def __init__(self,nome,tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def stato_apertura(self):
        if self.apertura:
            print("Aperto")
        else:
            print("Chiuso")
    def apri_ristorante(self):
        self.apertura = True
        print("Il ristorante è ora aperto!")
    def chiudi_ristorante(self):
        self.apertura = False
        print("Il ristorante è ora chiuso!")
    def aggiungi_menu(self):
        cibo = input("Indicare pietanza: ")
        prezzo = input("Indicare il prezzo: ")
        self.menu[cibo] = prezzo
    def togli_menu(self):
        cibo = input("indicare pietanza da eliminare: ")
        if cibo in self.menu:
            self.menu.pop(cibo)
            print("Eliminato con successo")
        else:
            print("Cibo non trovato")
    def stampa_menu(self):
        if self.menu == {}:
            print("Il menu è vuoto")
        else:    
            for i in self.menu:
                print(i,"Prezzo:",self.menu[i])
    def descrivi_ristorante(self):
        print(f"Questo ristorante si chiama {self.nome} e la tipologia della cucina è: {self.tipo_cucina}")


rist1 = Ristorante("Stella","Pizzeria")

