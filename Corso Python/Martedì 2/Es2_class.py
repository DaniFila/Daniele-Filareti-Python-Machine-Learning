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
        self.dizionario = {"Elettronica":0,"Abbigliamento":0}  #attributi dell'istanza
        self.prodotti_in_fabbrica = []
        self.tipologia_prodotti = []
        self.num_prodotti = {}
    def aggiungi_prodotto(self): # metodo per aggiungere prodotto
        nome = input("Indicare nome prodotto: ")
        costo_produzione = int(input("Indicare costo_produzione "))
        prezzo_vendita = int(input("Indicare prezzo di vendita "))
        n_prod = int(input("Indicare il numero di prodotti"))
        prod = Prodotto(nome,costo_produzione,prezzo_vendita)  # mi crea l'oggetto prodotto
        self.num_prodotti[prod] = n_prod
        while True:
            tipo = input("Indicare tipologia prodotto\n1: elettronica\n2:abbigliamento\n") # si chiede la tipologia del prodotto
            if tipo == "1":
                self.prodotti_in_fabbrica.append(prod)  # si aggiunge in lista prodotti_in_fabbrica il prodotto
                self.tipologia_prodotti.append(Elettronica(prod)) # si aggiunge in lista tipologia_prodotti l'oggetto prodotto con la tipologia 
                self.dizionario["Elettronica"] += n_prod # si aggiorna al dizionario il contatore
                print("Aggiunto con successo")
                break
            elif tipo == "2":
                self.prodotti_in_fabbrica.append(prod) # si aggiunge in lista prodotti_in_fabbrica il prodotto
                self.tipologia_prodotti.append(Abbigliamento(prod)) # si aggiunge in lista tipologia_prodotti l'oggetto prodotto con la tipologia 
                self.dizionario["Abbigliamento"] += n_prod # si aggiorna al dizionario il contatore
                print("Aggiunto con successo")
                break
            else:
                print("Scelta non valida")    # se non si digita 1 oppure 2 si ripete
    def vendi_prodotti(self): # metodo per vendere prodotto
        p = False
        a = input("Indicare nome prodotto: ") # si indica il prodotto
        for i in self.prodotti_in_fabbrica: 
            if i.nome == a: # se il nome corrisponde al nome di un oggetto prodotto nella lista
                p = True
                print("Il profitto è:",i.calcola_profitto()) # si stampa il profitto
                if self.num_prodotti[i] != 0:
                    self.num_prodotti[i] -=1
                    print("Prodotto venduto con successo!")
                    for j in self.tipologia_prodotti: 
                        if i == j.prodotto: # se l'oggetto prodotto corrisponde all'oggetto prodotto della tipologia 
                            if type(j) == Abbigliamento: # se è tipo abbigliamento
                                self.tipologia_prodotti.remove(j) # si rimuove dalla lista tipologia
                                self.dizionario["Abbigliamento"] -=1 # si aggiorna il dizionario
                            else:
                                self.tipologia_prodotti.remove(j) # sennò si rimuove dalla lista tipologia
                                self.dizionario["Elettronica"] -= 1 # si aggiorna il dizionario
                else:
                    print("Prodotto non disponibile")
        if not p:
            print("prodotto inesistente")
    def resi_prodotti(self):
        p = False # variabile booleana per verificare se il prodotto è stato trovato
        nome = input("indicare nome del prodotto da restituire: ")
        for i in self.prodotti_in_fabbrica:
            if nome == i.nome: # se il nome esiste nei prodotti della fabbrica
                p = True
                self.num_prodotti[i] += 1 # si incrementa il suo numero
                print("Prodotto restituito con successo!")
        if not p:
            print("Prodotto insesistente in fabbrica") # se non si trova il prodotto
            


    
        
f = Fabbrica()
f.aggiungi_prodotto()
f.aggiungi_prodotto()
print(f.num_prodotti)
f.vendi_prodotti()
print(f.num_prodotti)
f.resi_prodotti()
print(f.num_prodotti)


