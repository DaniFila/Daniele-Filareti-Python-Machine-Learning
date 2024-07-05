from random import randint
class Pokemon:
    def __init__(self):
        self.__nome=""
    def info(self):
        print(f"Il nome di questo pokemon è {self.nome}")
    def set_nome(self):
        self.__nome = input("Indicare il nome del Pokemon: ")

class Pikachù(Pokemon):
    razza = "Pikachù"
    tipo = "Elettro"
    hp = 50

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Fulmine":25}

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Fulmine\n")
            if a == "1":
                attacco = 20
                return attacco
            elif a == "2":
                attacco = 15
                return attacco
            elif a == "3":
                attacco = 25
                return attacco
            else:
                print("Errore")
    
    def info(self):
        super().info()
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Squirtle(Pokemon):
    razza = "Squirtle"
    tipo = "Acqua"
    hp = 60

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Pistol acqua":25}

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Pistol acqua\n")
            if a == "1":
                attacco = 20
                return attacco
            elif a == "2":
                attacco = 15
                return attacco
            elif a == "3":
                attacco = 25
                return attacco
            else:
                print("Errore")
    
    def info(self):
        super().info()
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Bulbasaur(Pokemon):
    razza = "Bulbasaur"
    tipo = "Erba"
    hp = 55

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Fendi foglia":25}

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Fendi foglia\n")
            if a == "1":
                attacco = 20
                return attacco
            elif a == "2":
                attacco = 15
                return attacco
            elif a == "3":
                attacco = 25
                return attacco
            else:
                print("Errore")
    
    def info(self):
        super().info()
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")

class Charmander(Pokemon):
    razza = "Charmander"
    tipo = "Fuoco"
    hp = 45

    def __init__(self):
        Pokemon.__init__(self)
        self.iv = randint(1,32)
        self.hp = self.hp + self.iv
        self.mosse = {"Azione":20,"Attacco Rapido":15,"Lancia fiamme":25}

    def attacca(self):
        attacco = 0
        while True:
            a = input("Seleziona:\n1: Azione\n2: Attacco Rapido\n3: Lancia fiamme\n")
            if a == "1":
                attacco = 20
                return attacco
            elif a == "2":
                attacco = 15
                return attacco
            elif a == "3":
                attacco = 25
                return attacco
            else:
                print("Errore")
    
    def info(self):
        super().info()
        print(f"La sua razza è {self.razza}, il suo tipo è {self.tipo},i suoi hp sono: {self.hp}")





    








    
    

    
    
    
