import pandas as pd
import numpy as np

class Vendite:
    def __init__(self):
        self.prodotto = ["Laptop","Smartphone","Tablet","Smartwatch","Televisore","Cuffie","Fotocamera","Stampante","Router","Monitor"]
        self.città = ["Roma", "Milano", "Napoli"]
        self.df = self.genera_dataframe()
    def genera_dataframe(self):
        data = {"Prodotto":np.random.choice(self.prodotto,10),
                "Quantità":np.random.randint(0,10,10),
                "Prezzo Unitario":np.random.randint(50,300,10),
                "Città":np.random.choice(self.città,10)}
        df = pd.DataFrame(data)
        return df
    def aggiungi_totale_vendite(self):
        self.df["Totale Vendite"] = self.df["Quantità"] * self.df["Prezzo Unitario"]
        print("Colonna aggiunta con successo!")
    def raggruppa_vendite_per_prodotto(self):
        vendite_per_prodotto = self.df.groupby("Prodotto")["Totale Vendite"].sum()
        print(f"Dataframe raggruppato per vendite prodotto:\n{vendite_per_prodotto}")
    def prodotto_più_venduto_su_quantità(self):
        quantita_per_prodotto = self.df.groupby("Prodotto").agg({"Quantità": "sum"}) # agg si utilizza con grupby ed è un metodo di aggregazione indicando nel dizionario la colonna come chiave e come valore la funzione di aggregazione
        prodotto_piu_venduto = quantita_per_prodotto.loc[quantita_per_prodotto["Quantità"].idxmax()] # loc è per selezionare righe in base a una etichetta
        print(f"Il prodotto più venduto è: {prodotto_piu_venduto}") 
    def città_con_maggior_volume_vendite_tot(self):
        città_volume_vendite = self.df.groupby("Città").agg({"Totale Vendite":"sum"})
        città_maggiore = città_volume_vendite.loc[città_volume_vendite["Totale Vendite"].idxmax()]
        print(f"La città con maggior volume di vendite totali è:\n{città_maggiore}")
    def nuovo_dataframe_filtrato(self):
        
    
a = Vendite()
a.genera_dataframe()
a.aggiungi_totale_vendite()
#a.raggruppa_vendite_per_prodotto()
a.prodotto_più_venduto_su_quantità()
a.città_con_maggior_volume_vendite_tot()
