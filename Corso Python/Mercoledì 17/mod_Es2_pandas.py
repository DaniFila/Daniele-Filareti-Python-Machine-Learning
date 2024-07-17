import pandas as pd
import numpy as np

class Vendite:
    def __init__(self): # classe costruttore dove al suo interno inserisco liste con prodotti, città e richiamo il metodo genera_dataframe per assegnare a df il dataframe
        self.prodotto = ["Laptop","Smartphone","Tablet","Smartwatch","Televisore","Cuffie","Fotocamera","Stampante","Router","Monitor"]
        self.città = ["Roma", "Milano", "Napoli"]
        self.df = self.genera_dataframe()
    def genera_dataframe(self): # metodo per generare dataframe
        data = {"Prodotto":np.random.choice(self.prodotto,10),
                "Quantità":np.random.randint(0,10,10),
                "Prezzo Unitario":np.random.randint(50,300,10),
                "Città":np.random.choice(self.città,10)}
        df = pd.DataFrame(data)
        return df
    def aggiungi_totale_vendite(self): # metodo per aggiungere colonna vendite totale
        self.df["Totale Vendite"] = self.df["Quantità"] * self.df["Prezzo Unitario"]
        print("Colonna aggiunta con successo!")

    def raggruppa_vendite_per_prodotto(self): # metodo per raggruppare vendite per prodotto
        vendite_per_prodotto = self.df.groupby("Prodotto")["Totale Vendite"].sum()
        print(f"Dataframe raggruppato per vendite prodotto:\n{vendite_per_prodotto}")

    def prodotto_più_venduto_su_quantità(self):# metodo per visualizare prodotto più venduto in base alla quantità
        quantita_per_prodotto = self.df.groupby("Prodotto").agg({"Quantità": "sum"}) # agg si utilizza con grupby ed è un metodo di aggregazione indicando nel dizionario la colonna come chiave e come valore la funzione di aggregazione
        prodotto_piu_venduto = quantita_per_prodotto.loc[quantita_per_prodotto["Quantità"].idxmax()] # loc è per selezionare righe in base a una etichetta
        print(f"Il prodotto più venduto è: {prodotto_piu_venduto}") 

    def città_con_maggior_volume_vendite_tot(self): # metodo per visualizzare la città con il maggior volume di vendite totali
        città_volume_vendite = self.df.groupby("Città").agg({"Totale Vendite":"sum"})
        città_maggiore = città_volume_vendite.loc[città_volume_vendite["Totale Vendite"].idxmax()]
        print(f"La città con maggior volume di vendite totali è:\n{città_maggiore}")

    def nuovo_dataframe_filtrato(self): # metodo per filtrare le vendite totali su un numero
        filtro = int(input("Indicare filtro vendite: "))
        nuovo_dataframe = self.df.loc[self.df["Totale Vendite"]>filtro]
        print(f"Nuovo dataframe con vendite superiori a {filtro}:\n{nuovo_dataframe}")

    def ordina_tot_vendite_desc(self): # metodo per ordinare il totale delle vendite in maniera decrescente
        self.df = self.df.sort_values(by="Totale Vendite",ascending=False) # il sort value ci permette di ordinare i valori specificando con by la colonna e con ascending l'ordinamento
        print(f"Ordinato con successo per Totale Vendite!\n{self.df}")
        
    def visualizza_vendite_per_città(self): # metodo per visualizzare le vendite totali di tutte le città
        vendite_per_città = self.df.groupby("Città").agg({"Totale Vendite":"sum"})
        print(vendite_per_città)




