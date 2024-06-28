class Calciatore:
    Calciatori = 0
    def __init__(self,nome,ruolo,valore):
        self.nome = nome
        self.ruolo = ruolo
        self.valore = valore
        Calciatore.Calciatori += 1
    def __str__(self):
        return f"Nome:{self.nome},,Ruolo:{self.ruolo},Valore: {self.valore}"
    def valori_calciatori(self):
        print(self.valore)

    def set_valore_calciatore(self):
        self.valore = input("Inserire valore calciatore: ")


ronaldo = Calciatore("Cristiano Ronaldo","Attaccante",10)
messi = Calciatore("Leo Messi","Attaccante",9)
buffon = Calciatore("Gigi Buffon","Portiere",9)

if ronaldo.valore>=messi.valore:
    if ronaldo.valore>=buffon.valore:
        print(ronaldo)
    else:
        print(buffon)
elif messi.valore >=ronaldo.valore:
    if messi.valore >= buffon.valore:
        print(messi)
    else:
        print(buffon)
