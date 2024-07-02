class Vendite:
    vendite = []
    def aggiungi_rapporto(self):
        p = True
        while p:
            vendita = []
            a = input("Inserire una serie di importi separati dallo spazio: ")
            vendita = a.split(" ")
            while True:
                for i in vendita:
                    try: 
                        self.vendite.append(int(i))
                    except ValueError:
                        print("Inseriti valori non validi!")
                        self.vendite = []
                        break
                break
            if self.vendite != []:
                p = False
    def totale_e_media(self):
        if self.vendite == []:
            print("Nessun rapporto vendite!")
        else:
            totale = sum(self.vendite)
            print(f"Il totale delle vendite è {totale} e la media delle vendite è {totale/len(self.vendite)} ")
    def vendite_sopra_media(self):
        copy_l_vendite = self.vendite
        l_giorno = []
        if self.vendite == []:
            print("Nessun rapporto vendite!")
        else:
            media = sum(self.vendite)/len(self.vendite)
            print(media)
            for i in range(len(copy_l_vendite)-1):
                if copy_l_vendite[i] >= media:
                    l_giorno.append(i+1)
                    copy_l_vendite.remove(copy_l_vendite[i])
            if l_giorno == []:
                print("Non c'è alcun giorno che supera la media delle vendite!")
            else:
                for i in l_giorno:
                    print(f"Nel giorno {i} le vendite hanno superato la media")
    def operazioni(self):
        a = input("Indicare operazione\n1: totale e media\n2: vendite sopra la media\n")
        while True:
            if a == "1":
                self.totale_e_media()
                break
            elif a == "2":
                self.vendite_sopra_media()
                break
            else:
                print("operazione non valida")                    


                

  

