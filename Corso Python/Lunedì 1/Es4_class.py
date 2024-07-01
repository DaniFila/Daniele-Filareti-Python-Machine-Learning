class Ristorante:  
    menu = {}    # dizionario per inserire pietanze con relativo prezzo
    apertura = False  # booleano per verificare apertura/chiusura ristorante
    def __init__(self,nome,tipo_cucina):  # parametri per creare gli oggetti
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def stato_apertura(self):  # funzione per verificare stato apertura attraverso booleano apertura
        if self.apertura:
            print("Aperto")
        else:
            print("Chiuso")
    def apri_ristorante(self): # funzione per aprire ristorante e impostare booleano a True
        self.apertura = True
        print("Il ristorante è ora aperto!")
    def chiudi_ristorante(self): # funzione per chiudere ristorante e impostare booleano a False
        self.apertura = False
        print("Il ristorante è ora chiuso!")
    def aggiungi_menu(self):   # funzione per aggiungere pietanza al dizionario menu con il prezzo
        cibo = input("Indicare pietanza: ")
        prezzo = input("Indicare il prezzo: ")
        self.menu[cibo] = prezzo
    def togli_menu(self):  # funzione per eliminare pietanza dal menu dizionario
        cibo = input("indicare pietanza da eliminare: ")
        if cibo in self.menu:
            self.menu.pop(cibo)
            print("Eliminato con successo")
        else:
            print("Cibo non trovato")
    def stampa_menu(self):  # funzione per stampare menu se non è vuoto con verifica e avviso eventuale
        if self.menu == {}:
            print("Il menu è vuoto")
        else:    
            for i in self.menu:
                print(i,"Prezzo:",self.menu[i])
    def descrivi_ristorante(self):  # funzione che descrive il ristorante indicando il nome e la tipologia di cucina
        print(f"Questo ristorante si chiama {self.nome} e la tipologia della cucina è: {self.tipo_cucina}")


rist1 = Ristorante("Stella","Pizzeria")

