class Animale:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
 
    



class Leone(Animale):
    cacciatore = False
    def __init__(self,nome,eta):
        Animale.__init__(self,nome,eta)
    def caccia(self):
        if self.cacciatore:
            print(f"Il leone di nome {self.nome} sta cacciando")
        else:
            print(f"Il leone di nome {self.nome} non sta cacciando")
            self.cacciatore = True
    def stato_caccia(self):
        if self.cacciatore:
            self.cacciatore = False
        else:
            self.cacciatore = True
        print("Stato cambiato")
    def fai_suono(self):
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono grgrgr")
    

class Giraffa(Animale):
    def __init__(self,nome,eta,altezza):
        self.alt = altezza
        Animale.__init__(self,nome,eta)
    def altezza(self):
        print(f"L'altezza della giraffa è: {self.alt}")
    def fai_suono(self):
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono auauauau")
    

class Pinguino(Animale):
    def __init__(self,nome,eta,carattere):
        self.carattere = carattere
        Animale.__init__(self,nome,eta)
    def carattere(self):
        print(f"Il carattere del pinguino è: {self.carattere}")
    def fai_suono(self):
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono tutututu")
    


