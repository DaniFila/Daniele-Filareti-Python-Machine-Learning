class Animale: # classe padre
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
 
    



class Leone(Animale): # classe figlia
    cacciatore = False
    def __init__(self,nome,eta):
        Animale.__init__(self,nome,eta) # eredita classe padre Animale
    def caccia(self): # metodo per stampare lo stato del leone di caccia
        if self.cacciatore:
            print(f"Il leone di nome {self.nome} sta cacciando")
        else:
            print(f"Il leone di nome {self.nome} non sta cacciando")
            self.cacciatore = True
    def stato_caccia(self): # metodo per cambiare stato caccina
        if self.cacciatore:
            self.cacciatore = False
        else:
            self.cacciatore = True
        print("Stato cambiato")
    def fai_suono(self): # metodo per stampare suono del leone
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono grgrgr")
    

class Giraffa(Animale): #classe figlia
    def __init__(self,nome,eta,altezza):
        self.alt = altezza
        Animale.__init__(self,nome,eta) # eredita classe padre Animale
    def altezza(self): # metodo che stampa l'altezza della giraffa
        print(f"L'altezza della giraffa è: {self.alt}") 
    def fai_suono(self): # metodo per stampare suono
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono auauauau")
    

class Pinguino(Animale): # classe figlia
    def __init__(self,nome,eta,carattere): 
        self.carattere = carattere
        Animale.__init__(self,nome,eta) # eredita classe padre Animale
    def carattere(self): # metodo per stampare carattere del pinguino
        print(f"Il carattere del pinguino è: {self.carattere}")
    def fai_suono(self): # metodo per stampare suono del pinguino
        print(f"L'animale {self.nome} con età di {self.eta} fa un suono tutututu")
    


# test

lion = Giraffa("leone",55,25)

lion.altezza()
        