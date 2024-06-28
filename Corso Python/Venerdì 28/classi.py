class Studenti:
    corpo_studentesco = 0
    ore_settimanali = 36
    def __init__(self,nome,cognome,voti):  # costruttore, costruisce gli attributi della classe, self sta per istanza
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
        Studenti.corpo_studentesco+=1
    def __str__(self):
        return f"Nome:{self.nome},Cognome:{self.cognome},Voti:{self.voti},Ore settimanali: {self.ore_settimanali}"

    def visualizza_nome(self):  # metodo getter
        print(self.nome)

    def inserisci_nome(self):  # metodo setter
        self.nome = input("Inserisci nome: ")

    
daniele = Studenti("Daniele","Filareti",[10,8])
aurora = Studenti("Aurora","Russo",[9,10])

#print(daniele.nome)
#print(daniele.cognome)
#print(daniele.voti)

#print(aurora.nome)
#print(aurora.cognome)
#print(aurora.voti)

daniele.ore_settimanali +=5

print(daniele)


