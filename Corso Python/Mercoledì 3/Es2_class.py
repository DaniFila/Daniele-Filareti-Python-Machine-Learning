class UnitaMilitare:
    difesa = 0
    calibrazione = 0 
    esplorazione = 0
    rifornimento = {}
    conduzione = 0
    def __init__(self,nome,numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità militare {self.nome} si sta muovendo...")
    
    def attacca(self):
        print(f"L'unità militare {self.nome} con {self.numero_soldati} sta attaccando...")

    def ritira(self):
        pass


class Fanteria(UnitaMilitare):
    classe = "Fanteria"
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.__init__(self,nome, numero_soldati)
    def costruisci_trincea(self):
        print("E' stata costruita una trincea...")
        self.difesa +=1

class Ricognizione(UnitaMilitare):
    classe = "Ricognizione"
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.__init__(self,nome, numero_soldati)




class SupportoLogistico(UnitaMilitare):
    classe = "SupportoLogistico"
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.__init__(self,nome, numero_soldati)

class Cavalleria(UnitaMilitare):
    classe = "Cavalleria"
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.__init__(self,nome, numero_soldati)
    def esplora_terreno(self):
        a = int(input("Quanto terreno vuoi esplorare? "))
        print(f"Sono stati esplorati {a}Km quadrati di terreno...")
        self.esplorazione += a
    def rifornisci_unità(self):
        a = input("Indicare tipo di rifornimento: ")
        b = input("Indicare quantità")
        if  a in self.rifornimento:
            self.rifornimento[a] += b
        else:
            self.rifornimento[a] = b
        print("Rifornimento avvenuto con successo!")

class Artiglieria(UnitaMilitare):
    classe = "Artiglieria"
    def __init__(self, nome, numero_soldati):
        UnitaMilitare.__init__(self,nome, numero_soldati)
    def calibra_artiglieria(self):
        print("E' stata calibrata l'artiglieria...")
        self.calibrazione += 1


class ControlloMilitare: # classe per controllo militare
    def __init__(self):
        self.unità_registrate = [] # lista per aggiungere unità
        self.tipo_unità = {"Fanteria": 0,"Artiglieria": 0,"Cavalleria": 0,"SupportoLogistico": 0,"Ricognizione": 0} # dizionario per tracciare numero unità per tipo
    def registra_unità(self,unità): # metodo per registrare unità passata
        self.unità_registrate.append(unità) # lo aggiunge alla lista
        tipologia_unita = unità.classe # salva il tipo in una variabile locale
        self.tipo_unità[tipologia_unita] += 1 # incrementa il conto del tipo sul dizionario

    def dettagli_unita(self, nome): # metodo per stampare i dettagli dell'unità passata
        for unità in self.unità_registrate:
            if unità.nome == nome:
                print(f"Dettagli dell'unità {nome}:")
                print(f"Nome: {unità.nome}")
                print(f"Numero di soldati: {unità.numero_soldati}")
                print(f"Tipo: {unità.classe}")
                return
        print(f"Unità con nome {nome} non trovata.")
    
    def mostra_unità_registrate(self): # metodo per mostrare numero di unità registrate con il rispettivo tipo
        for unità,numero in self.tipo_unità.items():
            print(f"Unità {unità}:{numero}")


fant = Fanteria("asse",25)
# fant.costruisci_trincea()
# fant.costruisci_trincea()
# print(fant.difesa)
contr = ControlloMilitare()

contr.registra_unità(fant)

# print(contr.tipo_unità)

# contr.dettagli_unita("asse")

contr.mostra_unità_registrate()          

    







    

    
