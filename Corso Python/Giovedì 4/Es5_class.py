class PersonalTrainer:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
        self.__stipendio = 0
    def info(self):
        print(f"{self.nome}, età: {self.età}")
    def __set(self,stip):
        self.__stipendio = stip
    def __get(self):
        return self.__stipendio
    def scrivi_scheda(self,atleta):
        scheda = {}
        while True:
            a = input("1: Petto\n2: Spalle\n3: Tricipiti\n4: Addominali\n5: Dorso\n6: Gambe\n7: Bicipiti\n8: Stop\n")
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
        atleta.scheda = scheda


class Atleta:
    scheda = {}
    def __init__(self,nome,età,sesso):
        self.nome = nome
        self.età = età
        self.sesso = sesso
        self.__pagamento = False
    def __set_stato_pagamento(self):
        if self.__pagamento:
            self.__pagamento = False
            print("il Cliente non ha pagato!")
        else:
            self.__pagamento = True
            print("Il Cliente ha pagato!")
    def __get_stato_pagamento(self):
        if self.__pagamento:
            print("Il Cliente risulta in regola con i pagamenti!")
        else:
            print("Il Cliente non risulta in regola con i pagamenti!")
    def visualizza_scheda(self):
        if self.scheda == {}:
            print("Non hai una scheda")
        else:
            for gruppo,esercizio in self.scheda.items():
                print(f"Gruppo muscolare: {gruppo} esercizi: {esercizio}")
    def info(self):
        print(f"{self.nome}, età: {self.età}, sesso: {self.sesso}")


class Datore(Atleta,PersonalTrainer):
    def __init__(self, nome, età, sesso):
        super().__init__(nome, età, sesso)
    def set_stipendio_personal(self,personal_trainer):
        personal_trainer._PersonalTrainer__set(int(input("Indicare stipendio: ")))
    def get_stipendio_persona_trainer(self,personal_trainer):
        print(personal_trainer._PersonalTrainer__get())
    def set_stato_pagamento_atleta(self,atleta):
        atleta._Atleta__set_stato_pagamento()
    def get_stato_pagamento_atleta(self,atleta):
        atleta._Atleta__get_stato_pagamento()
    def info(self):
        super().info()
        print("Ruolo: Datore")

class MenuPalestra:
    def menu(self):
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
    
boss = Datore("antonio",21,"maschio")
personal = PersonalTrainer("Samuele",25)
cliente = Atleta("Ronnie Coleman",50,"maschio")

menu = MenuPalestra()
menu.menu()





