import pandas as pd
import numpy as np

class ElencoUtenza():
    def __init__(self):
        self.df = self.genera_dataframe()
        self.nomi = ["Alessandro","Beatrice","Carlo","Daniele","Enrico","Francesca","Giulia","Leonardo","Martina","Nicola"]
        self.città =  ["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze","Venezia","Verona"]
    def genera_dataframe(self):
        data = {"Nome":np.random.choice(self.nomi,20),
                "Città":np.random.choice(self.città,20),
                "Età":np.random.randint(0,90,20),
                "Salario":np.random.randint(1000,10000,20)}
        df = pd.DataFrame(data)
        return df



a = ElencoUtenza()
a.genera_dataframe()
print(a.df)





def visualizza_prime_5_righe(df):
    d = df.head()
    print(f"Le prime 5 righe sono:\n{d}")

def visualizza_ultime_5_righe(df):
    d = df.tail()
    print(f"Le ultime 5 righe sono:\n{d}")


def visualizza_tipo_dati(df):
    tipo = df.dtypes
    print(f"I tipi di dati sono:\n{tipo}")


def descrivi_stato(df):
    descrivi = df.describe()
    print(f"Descrizione:\n{descrivi}")

def rimuovi_duplicati(df):
    df_senza_duplicati = df.drop_duplicates()
    print("Eventuali valori duplicati eliminati!")
    return df_senza_duplicati

def salva_in_csv(df):
    df.to_csv("Corso Python/Mercoledì 17/Es1.csv")
    print("Salvato con successo!")

def gestione_valori_mancanti(df):
    l = ["Nome","Città","Età","Salario"]
    for i in l:
        df[i] = df[i].fillna(df[i].median())
    print(f"Eventuali valori mancanti gestiti!")

"""def categorie_età_verifica(età):
    if età <= 18:
        return 'Giovane'
    elif età <= 65:
        return 'Adulto'
    else:
        return 'Senior'
    
def categorie_età(df):
    df['Categoria Età'] = categorie_età(df["Età"])"""


