import pandas as pd
import numpy as np

class ElencoUtenza():
    def __init__(self):
        self.nomi = ["Alessandro","Beatrice","Carlo","Daniele","Enrico","Francesca","Giulia","Leonardo","Martina","Nicola"]
        self.città =  ["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze","Venezia","Verona"]
        self.df = self.genera_dataframe()
    def genera_dataframe(self):
        data = {"Nome":np.random.choice(self.nomi,20),
                "Città":np.random.choice(self.città,20),
                "Età":np.random.randint(0,90,20),
                "Salario":np.random.randint(1000,10000,20)}
        df = pd.DataFrame(data)
        return df
    def visualizza_prime_5_righe(self):
        d = self.df.head()
        print(f"Le prime 5 righe sono:\n{d}")
    def visualizza_ultime_5_righe(self):
        d = self.df.tail()
        print(f"Le ultime 5 righe sono:\n{d}")
    def visualizza_tipo_dati(self):
        tipo = self.dtypes
        print(f"I tipi di dati sono:\n{tipo}")
    def descrivi_stato(self):
        descrivi = self.df.describe()
        print(f"Descrizione:\n{descrivi}")
    def rimuovi_duplicati(self):
        self.df = self.df.drop_duplicates()
        print("Eventuali valori duplicati eliminati!")
    def salva_in_csv(self):
        self.df.to_csv("Corso Python/Mercoledì 17/Es1.csv")
        print("Salvato con successo!")
    def gestione_valori_mancanti(self):
        l = ["Nome","Città","Età","Salario"]
        for i in l:
            self.df[i] = self.df[i].fillna(self.df[i].median())
        print(f"Eventuali valori mancanti gestiti!")
    def categorie_età_verifica(età): # funzione che verifica l'età e restituisce la stringa corrispondente della categoria
        if età <= 18:
            return 'Giovane'
        elif età <= 65:
            return 'Adulto'
        else:
            return 'Senior'
    def aggiungi_categorie_età_verifica(self): # funzione che richiama la funzione categorie_età_verifica e crea la colonna categorie età confrontando l'età e aggiungendo la categoria
        self.df["Categorie Età"] = self.df["Età"].apply(self.categorie_età_verifica)
        print("Categorie età aggiunta con successo!")



















