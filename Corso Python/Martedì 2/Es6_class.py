class MembroSquadra: # classe padre
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
    def descrivi(self): # metodo per descrivere membro giocatore
        print(f"Nome Giocatore: {self.nome}, Età: {self.età}")



class Giocatore(MembroSquadra): #classe figlia
    gioca = False
    def __init__(self, nome, età,ruolo,num_maglia): 
        MembroSquadra.__init__(self,nome, età)
        self.ruolo = ruolo
        self.num_maglia = num_maglia
    def gioca_partita(self): # metodo per cambiare stato del gioco
        if self.gioca == True:
            self.gioca = False
        else:
            self.gioca = True
        print("Stato cambiato!")
    def stato(self): # metodo per stampare lo stato del gioco
        if self.gioca == True:
            print(f"Il giocatore {self.nome} sta attualmente giocando")
        else:
            print(f"Il giocatore {self.nome} non sta attualmente giocando")
    def info(self): # metodo per stampare informazioni giocatore
        super().descrivi()
        print(f"ruolo:{self.ruolo}, numero maglia:{self.num_maglia}")
    

class Allenatore(MembroSquadra): # classe figlia
    def __init__(self, nome,età,anni_esperienza):
        Allenatore.__init__(self,nome,età)
        self.anni_esperienza = anni_esperienza
    def dirige_allenamento(self): # metodo per elogiare allenatore
        print(f"L'allenatore {self.nome},dirige gli allenamenti in maniera fantastica!")
    def info(self): # metodo per stampare informazioni allenatore
        super().descrivi()
        print(f"Anni di esperienza: {self.anni_esperienza}")


class Assistente(MembroSquadra): # classe figlia
    def __init__(self, nome, età,tipo):
        MembroSquadra.__init__(self,nome,età)
        self.tipo = tipo
    def info_assistenza(self): # metodo per stampare informazioni assistente
        super().descrivi()
        print(f"Il suo ruolo è assistente del tipo {self.tipo}")
    


