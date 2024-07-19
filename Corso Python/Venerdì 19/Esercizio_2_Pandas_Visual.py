import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        self.df = self.crea_df()

    def crea_df(self): # metodo per creare df con colonna Temperature prese randomiche
        data = {"Età":np.random.randint(0,100,30),
                "Altezza":np.random.randint(100,200,30),
                "Peso":np.random.randint(40,120,30)}
        df =pd.DataFrame(data)
        return df
    def normalizzazione(self):
        df_norm = self.df
        col = ["Altezza","Peso"]
        #for c in col:
            #df_norm[c] = (df_norm[c] - df_norm[c].min()) / df_norm[c].min() - df_norm[c].max()
        #print("Normalizzato!")

a = Data()
print(a.df)
a.normalizzazione()
print(a.df)