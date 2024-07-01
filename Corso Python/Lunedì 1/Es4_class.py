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
        tipologia = input("Indicare la sua tipologia: ")
        self.menu[cibo] = Cibo(cibo,tipologia,prezzo)  # mi salva nel dizionario l'oggetto cibo con le caratteristiche indicate in input
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
                print(self.menu[i])
    def descrivi_ristorante(self):  # funzione che descrive il ristorante indicando il nome e la tipologia di cucina
        print(f"Questo ristorante si chiama {self.nome} e la tipologia della cucina è: {self.tipo_cucina}")




class Cibo:
    def __init__(self,nome,tipologia,prezzo):  # parametri per creare oggetto cibo
        self.nome = nome
        self.tipologia = tipologia
        self.prezzo = prezzo

    def __str__(self):  # funzione della classe per andare a fare la stampa dell'oggetto str
        return f"Il nome di questa pietanza è: {self.nome}, la sua tipologia è: {self.tipologia}, il suo prezzo è: {self.prezzo}"




rist1 = Ristorante("Stella","Pizzeria")

rist1.aggiungi_menu()

rist1.stampa_menu()