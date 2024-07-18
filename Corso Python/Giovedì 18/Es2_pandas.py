import pandas as pd
import numpy as np

class Vendite:
    def __init__(self):
        self.prodotti = ["Laptop","Smartphone","Tablet","Smartwatch","Cuffie"]
        self.città = ["Roma","Milano","Firenze","Napoli"]
        self.date = ["2023-01-01", "2023-05-15","2023-07-22","2023-10-30","2023-12-25"]
        self.df = self.crea_df()
    def crea_df(self):
        data = {"Data":np.random.choice(self.date,10),
                "Città":np.random.choice(self.città,10),
                "Prodotto":np.random.choice(self.prodotti,10),
                "Quantità":np.random.randint(0,20,10)}
        df = pd.DataFrame(data)
        return df


class Costi(Vendite):
    def __init__(self):
        Vendite.__init__(self)
        self.df_costi = self.crea_df_costi()
    def crea_df_costi(self):
        data = {"Prodotto":np.random.choice(self.prodotti,10),
                "Costi":np.random.randint(10,50,10)}
        df = pd.DataFrame(data)
        return df
    

def unione(df1,df2):
    union = pd.merge(df1.df,df2.df, on="Prodotto")
    return union

def pivot(df):
    pivot = df.df.pivot_table(index='Prodotto', columns='Città', values="Quantità", aggfunc='sum')
    return pivot
df1 = Vendite()
df2 = Costi()
df1.crea_df()
df2.crea_df_costi()

df_unione = unione(df1,df2)
print(df_unione)
pivot = pivot(df1)
print(pivot)