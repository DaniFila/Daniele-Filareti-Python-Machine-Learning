class PersonaleCucina: # classe padre
    inventario = {}
    def __init__(self,nome,età): 
        self.nome = nome
        self.età = età
    def lavora(self): # metodo che stampa una descriione che sta lavorando 
        print(f"{self.nome} del personale cucina di età: {self.età}, sta lavorando")
    def aggiungi_inventario(self): # metodo per aggiungere piatto a inventario
        nome = input("Inserire piatto da aggiungere: ")
        quantità = int(input("Indicare quantità piatto: "))
        self.inventario[nome] = quantità
    def rimuovi_inventario(self): # metodo per ridurre quantità piatto a inventario
        nome = input("Inserire piatto: ")
        if nome in self.inventario:
            if self.inventario[nome] >0:
                self.inventario[nome] -=1
                print("Quantità piatto ridotta")
            else:
                print("Piatto non disponibile")
        else:
            print("Piatto assente")
    

class Chef(PersonaleCucina): # classe figlia
    def __init__(self, nome, età,specialità):
        PersonaleCucina.__init__(self,nome, età) # eredita attributi e metodi classe padre
        self.specialità = specialità
    def prepara_menu(self): # metodo che stampa un messaggio
        print(f"Lo Chef {self.nome} sta preparando il menù della giornata odierna!")
    def info_lavoro(self): # metodo delle info chef con richiamo metodo classe padre
        super().lavora()
        print(f"Il suo ruolo è: Chef, la sua personalità è: {self.specialità}")



class SousChef(PersonaleCucina): # classe figlia
    def __init__(self, nome, età): 
        PersonaleCucina.__init__(self,nome, età) # eredita attributi e metodi classe padre
    def gestisci_inventario(self): # metodo gestisci inventario con richiamo metodi classe padre
        while True:
            a = input("1: Aggiungi piatto a inventario\n2:Rimuovi piatto a inventario\n")
            if a == "1":
                super().aggiungi_inventario()
                break
            elif a == "2":
                super().rimuovi_inventario()
                break
            else:
                print("Operazione non valida")
    

class CuocoLinea(PersonaleCucina): # classe figlia
    def __init__(self, nome, età):
        PersonaleCucina.__init__(self,nome, età) # eredita attributi e metodi classe padre
    def cucina_piatto(self,piatto): # metodo per cucinare piatto e ridurre dall'inventario la quantità se è disponibile
        if piatto in self.inventario:
            if self.inventario[piatto] > 0:
                print(f"Il cuoco di linea di nome {self.nome}, sta cucinando il piatto: {piatto}")
                self.inventario[piatto] -= 1
            else:
                print("Piatto non disponibile")
        else:
            print("Piatto assente")











    