import pandas as pd 
import numpy as np

class Azienda:
    def __init__(self): # metodo costruttore dove creo una lista con date casuali e richiamo il metodo per creare il dataframe
        self.data = ['2024-01-15','2024-02-03','2024-03-10','2024-04-22','2024-05-05','2024-06-18','2024-07-29']
        self.df = self.crea_df()
    def crea_df(self): # metodo che crea il df
        data = {"Data":np.random.choice(self.data,30),
                "Vendite":np.random.randint(0,100,30),
                "Ore Lavorative":np.random.randint(4,10,30)}
        df = pd.DataFrame(data)
        df.to_csv("Azienda.csv")
        return df
    
    def vendite_medie_per_ora_giornaliere(self): # metodo che crea la colonna Vendite per ora Lavorativa
        self.df["Vendite per ora Lavorativa"] = self.df["Vendite"] / self.df["Ore Lavorative"]
        print("Colonna creata!")
        self.df.to_csv("Azienda.csv")
    def max_min_vendite_per_ora_lavorativa(self): # metodo che calcola la vendita maggiore e minore
        group = self.df.groupby("Data").agg({"Vendite per ora Lavorativa":"sum"})
        group.to_csv("Vendite_per_Data_Azienda.csv")
        max = group.idxmax()
        min = group.idxmin()
        max.to_csv("Max_vendita_Azienda.csv")
        min.to_csv("Min_Vendita_Azienda.csv")
        print(f"Il giorno con le vendite maggiori è:\n{max}\nIl giorno con le vendite minori è:\n{min}\n")



def menu(): # funzione menu che stampa le scelte e chiede in input la scelta
    info = """1: Visualizza DataFrame
2: Crea Colonna Vendite per Ora Lavorativa
3: Individa il Giorno Massimo e Minimo di Vendite per Ora Lavorativa
0: Exit
"""
    s = input(info)
    return s

def main(): # funzione main che richiama tutte le altre funzioni, metodi e classi
    a = Azienda()
    while True:
        s = menu()
        if s == "1":
            print(f"Dataset\n{a.df}")
        elif s == "2":
            a.vendite_medie_per_ora_giornaliere()
        elif s == "3":
            try:
                a.max_min_vendite_per_ora_lavorativa()
            except:
                print("Creare prima colonna Vendite per Ora Lavorativa!")
        elif s == "4":
            break
        else:
            print("Error")

main()