import pandas as pd
import numpy as np


def genera_dataframe():
    nomi = ["Alessandro","Beatrice","Carlo","Daniele","Enrico","Francesca","Giulia","Leonardo","Martina","Nicola"]
    città =  ["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze","Venezia","Verona"]
    data = {"Nome":np.random.choice(nomi,20),
            "Città":np.random.choice(città,20),
            "Età":np.random.randint(0,90,20),
            "Salario":np.random.randint(1000,10000,20)}
    df = pd.DataFrame(data)
    return df

def visualizza_prime_5_righe(df):
    d = df.head()
    print(f"Le prime 5 righe sono:\n{d}")

def visualizza_ultime_5_righe(df):
    d = df.tail()
    print(f"Le ultime 5 righe sono:\n{d}")

df = genera_dataframe()


def visualizza_tipo_dati(df):
    tipo = df.dtypes
    print(f"I tipi di dati sono:\n{tipo}")


def descrivi_stato(df):
    descrivi = df.describe()
    print(f"Descrizione:\n{descrivi}")

def rimuovi_duplicati(df):
    df_senza_duplicati = df.drop_duplicates()
    return df_senza_duplicati



print(df)
df = rimuovi_duplicati(df)
print()
print(df)
