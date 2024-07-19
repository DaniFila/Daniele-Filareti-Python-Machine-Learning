import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        self.df,self.data = self.crea_df()

    def crea_df(self): # metodo per creare df con colonna Temperature prese randomiche
        data = {"Età":np.random.randint(0,100,30),
                "Altezza":np.random.randint(100,200,30),
                "Peso":np.random.randint(40,120,30)}
        df =pd.DataFrame(data)
        return df,data
    def normalizzazione(self):
        df_norm = pd.DataFrame(self.data)
        col = ["Altezza","Peso"]
        for c in col:
            df_norm[c] = (df_norm[c] - df_norm[c].min()) / (df_norm[c].max() - df_norm[c].min())
        return df_norm
    def visualizza(self):
        df_norm = self.normalizzazione()
        plt.figure()
        plt.plot(self.df, df_norm)
        plt.title('Grafico a Linee')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.show()

a = Data()
a.normalizzazione()
a.visualizza()