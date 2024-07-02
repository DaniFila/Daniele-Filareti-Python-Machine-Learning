class Prodotto:
    def __init__(self,nome,costo_produzione,prezzo_vendita):  # attributi dell'istanza
        self.nome = nome  
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    def calcola_profitto(self): # metodo che ritorna il profitto
        a = self.prezzo_vendita-self.costo_produzione
        return a
    def __str__(self):  # metodo per descrizione prodotto
        return f"{self.nome} costo di produzione: {self.costo_produzione}, il prezzo di vendita è {self.prezzo_vendita}"
    



class Elettronica:
    def __init__(self,prodotto): # attributi dell'istanza
        self.prodotto = prodotto
        self.garanzie = 0
    def garanzia(self,g): # metodo per dare la garanzia
        self.garanzia = g


class Abbigliamento:
    def __init__(self,prodotto): # attributi dell'istanza
        self.prodotto = prodotto
        self.materiali = "non definito" 
    def materiale(self,m): # metodo per indicare materiale
        self.materiali = m




class Fabbrica:
    def __init__(self):
        self.dizionario = {"Elettronica":0,"Abbigliamento":0}
        self.prodotti_in_fabbrica = []
        self.tipologia_prodotti = []
    def aggiungi_prodotto(self):
        nome = input("Indicare nome prodotto: ")
        costo_produzione = int(input("Indicare costo_produzione "))
        prezzo_vendita = int(input("Indicare prezzo di vendita "))
        prod = Prodotto(nome,costo_produzione,prezzo_vendita)
        while True:
            tipo = input("Indicare tipologia prodotto\n1: elettronica\n2:abbigliamento\n")
            if tipo == "1":
                self.prodotti_in_fabbrica.append(prod)
                self.tipologia_prodotti.append(Elettronica(prod))
                self.dizionario["Elettronica"] += 1
                print("Aggiunto con successo")
                break
            elif tipo == "2":
                self.prodotti_in_fabbrica.append(prod)
                self.tipologia_prodotti.append(Abbigliamento(prod))
                self.dizionario["Abbigliamento"] += 1
                print("Aggiunto con successo")
                break
            else:
                print("Scelta non valida")   
    def vendi_prodotti(self):
        a = input("Indicare nome prodotto: ")
        for i in self.prodotti_in_fabbrica:
            if i.nome == a:
                print(i.calcola_profitto())
                for j in self.tipologia_prodotti:
                    if i == j.prodotto:
                        if type(j) == Abbigliamento:
                            self.tipologia_prodotti.remove(j)
                            self.dizionario["Abbigliamento"] -=1
                        else:
                            self.tipologia_prodotti.remove(j)
                            self.dizionario["Elettronica"] -= 1
                self.prodotti_in_fabbrica.remove(i)
            else:
                print("prodotto non disponibile")
    # def resi_prodotto(self):


    
        
f = Fabbrica()
f.aggiungi_prodotto()
f.aggiungi_prodotto()
print(f.dizionario)
f.vendi_prodotti()
print(f.dizionario)

