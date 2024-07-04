class PersonalTrainer: # classe personaltrainer 
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
        self.__stipendio = 0
    def info(self): # metodo che stampa informazioni
        print(f"{self.nome}, età: {self.età}")
    def __set(self,stip): # metodo privato per impostare stipendio personal trainer
        self.__stipendio = stip
    def __get(self): # metodo privato per avere stipendio personal
        return self.__stipendio
    def scrivi_scheda(self,atleta): # metodo per scrivere scheda per un atleta che si passa nel metodo
        scheda = {} # la scheda sarà un dizionario con chiave il gruppo muscolare e valore una lista con esercizi con ripetizioni e serie
        while True:
            a = input("1: Petto\n2: Spalle\n3: Tricipiti\n4: Addominali\n5: Dorso\n6: Gambe\n7: Bicipiti\n8: Stop\n") # si indica quale gruppo muscolare
            if a == "1":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni ")
                    l.append(y)
                scheda["Petto"] = l
            elif a == "2":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Spalle"] = l
            elif a == "3":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Tricipiti"] = l
            elif a == "4":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Addominali"] = l
            elif a == "5":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Dorso"] = l
            elif a == "6":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Gambe"] = l
            elif a == "7":
                l = []
                n = int(input("Inserire numero di esercizi: "))
                for i in range(n):
                    y = input("Inserire nome esercizio, serie e ripetizioni: ")
                    l.append(y)
                scheda["Bicipiti"] = l
            elif a == "8":
                print("Grazie e arrivederci!")
                break
            else:
                print("Error")
        atleta.scheda = scheda # qui si imposta la scheda dell'atleta con quella appena creata


class Atleta: # classe atleta
    scheda = {}  # scheda in dizionario
    def __init__(self,nome,età,sesso):
        self.nome = nome
        self.età = età
        self.sesso = sesso
        self.__pagamento = False
    def __set_stato_pagamento(self): # metodo privato per impostare se lo stato di pagamento è true quindi ha pagato oppure no
        if self.__pagamento:
            self.__pagamento = False
            print("il Cliente non ha pagato!")
        else:
            self.__pagamento = True
            print("Il Cliente ha pagato!")
    def __get_stato_pagamento(self): # metodo privato che stampa lo stato del pagamento
        if self.__pagamento:
            print("Il Cliente risulta in regola con i pagamenti!")
        else:
            print("Il Cliente non risulta in regola con i pagamenti!")
    def visualizza_scheda(self): # metodo per visualizzare scheda
        if self.scheda == {}:
            print("Non hai una scheda")
        else:
            for gruppo,esercizio in self.scheda.items():
                print(f"Gruppo muscolare: {gruppo} esercizi: {esercizio}")
    def info(self): # metodo per visualizzare info
        print(f"{self.nome}, età: {self.età}, sesso: {self.sesso}")


class Datore(Atleta,PersonalTrainer): # classe del datore di lavoro 
    def __init__(self, nome, età, sesso):
        super().__init__(nome, età, sesso)
    def set_stipendio_personal(self,personal_trainer): # metodo per impostare stipendio personal trainer passato nel metodo
        personal_trainer._PersonalTrainer__set(int(input("Indicare stipendio: ")))
    def get_stipendio_persona_trainer(self,personal_trainer): # metodo per visualizzare lo stipendio del personal tranier passato nel metodo
        print(personal_trainer._PersonalTrainer__get())
    def set_stato_pagamento_atleta(self,atleta): # metodo per impostare lo stato di pagamento dell'atleta passato nel metodo
        atleta._Atleta__set_stato_pagamento()
    def get_stato_pagamento_atleta(self,atleta): # metodo per visualizzare lo stato del pagamento dell'atleta passato nel metodo
        atleta._Atleta__get_stato_pagamento()
    def info(self): # metodo per visualizzare info
        super().info() 
        print("Ruolo: Datore")


# questa classe è dimostrativa per testare le classi Atleta,PersonalTrainer e Datore, il test è effettuato attraverso 3 oggetti creati nel codice
class MenuPalestra: # classe per avere un menù
    def menu(self): # metodo dove si selezione il tipo di ruolo e in base al tipo si effettuano varie operazioni
        while True:
            a = input("Indicare tipologia ruolo:\n1: Cliente\n2: Personal Trainer\n3: Datore\n4: Exit\n")
            if a == "1":
                while True:
                    b = input("Indicare azione:\n1: Visualizza scheda\n2: Visualizza le tue info\n3: Exit\n")
                    if b == "1":
                        cliente.visualizza_scheda()
                    elif b == "2":
                        cliente.info()
                    elif b == "3":
                        break
                    else:
                        print("Error")
            elif a == "2":
                while True:
                    b = input("Indicare azione:\n1: scrivi scheda\n2: Visualizza le tue info\n3: Exit\n")
                    if b == "1":
                        personal.scrivi_scheda(cliente)
                    elif b == "2":
                        personal.info()
                    elif b == "3":
                        break
                    else:
                        print("Error")
            elif a == "3":
                while True:
                    b = input("Indicare azione:\n1: imposta stipendio personal trainer\n2: Visualizza stipendio personal trainer\n3:Cambia stato pagamento cliente\n4: visualizza stato pagamento cliente\n5: Exit\n")
                    if b == "1":
                        boss.set_stipendio_personal(personal)
                    elif b == "2":
                        boss.get_stipendio_persona_trainer(personal)
                    elif b == "3":
                        boss.set_stato_pagamento_atleta(cliente)
                    elif b == "4":
                        boss.get_stato_pagamento_atleta(cliente)
                    elif b == "5":
                        break
                    else:
                        print("Error")
            elif a == "4":
                print("Arrivederci")
                break
            else:
                print("Error")


 # creazione oggetti per test   
boss = Datore("antonio",21,"maschio")
personal = PersonalTrainer("Samuele",25)
cliente = Atleta("Ronnie Coleman",50,"maschio")

menu = MenuPalestra()
menu.menu() # richiamo del test





