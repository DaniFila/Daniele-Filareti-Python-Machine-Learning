import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Temperature:
    def __init__(self): # metodo costruttore dove richiamo metodo per creare df
        self.df = self.crea_df()

    def crea_df(self): # metodo per creare df con colonna Temperature prese randomiche
        data = {"Temperature":np.random.randint(0,40,30)}
        df =pd.DataFrame(data)
        return df
    
    def temp_max(self): # metodo che restituisce la temperatura massima
        max = self.df["Temperature"].max()
        return max
    def temp_min(self): # metodo che restituisce la temperatura minima
        min = self.df["Temperature"].min()
        return min
    def temp_mean(self): # metodo che restituisce la temperatura media
        mean = self.df["Temperature"].mean()
        return mean
    def temp_median(self): # metodo che restituisce la mediana della temperatura
        median = self.df["Temperature"].median()
        return median
    def print_stats(self): # metodo che visualizza un grafico a barre con tutte le statistiche del max,min,median,mean
        max = self.temp_max()
        min = self.temp_min()
        mean = self.temp_mean()
        median = self.temp_median()
        cat = ["MAX","MIN","MEAN","MEDIAN"]
        val = [max,min,mean,median]
        plt.figure()
        plt.bar(cat, val)
        plt.title('STATISTICHE')
        plt.xlabel('TIPOLOGIA')
        plt.ylabel('GRADI')
        plt.show()

    
def main(): # funzione che richiede se si vogliono visualizzare le statistiche
    a = Temperature()
    s = input("Vuoi visualizzare statistiche? ").lower()
    if s == "si":
        a.print_stats()
    else:
        print("Arrivederci!")


main()