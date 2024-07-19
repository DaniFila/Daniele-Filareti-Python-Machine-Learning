import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Temperature:
    def __init__(self):
        self.df = self.crea_df()

    def crea_df(self):
        data = {"Temperature":np.random.randint(0,40,30)}
        df =pd.DataFrame(data)
        return df
    
    def temp_max(self):
        max = self.df["Temperature"].idxmax()
        return max
    def temp_min(self):
        min = self.df["Temperature"].idxmin()
        return min
    def temp_mean(self):
        mean = self.df["Temperature"].mean()
        return mean
    def temp_median(self):
        median = self.df["Temperature"].median()
        return median
    def print_stats(self):
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
        plt.ylabel('Valori')
        plt.show()

    
def main():
    a = Temperature()
    s = input("Vuoi visualizzare statistiche? ").lower()
    if s == "si":
        a.print_stats()
    else:
        print("Arrivederci!")


main()