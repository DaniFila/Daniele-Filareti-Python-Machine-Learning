import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class Housing:
    etichette = ["crim", "zn", "indus", "chs", "nox", "rm", "età", "dis", "rad", "tax", "ptratio", "bk", "lstat%", "medv"]
    def __init__(self,nome_file):
        self.df = pd.read_csv(nome_file,sep="\s+",names=self.etichette)
        self.nome_file = nome_file
    def scrivi_csv(self):
        self.df.to_csv("Corso Python/Martedì 23/housing_pulito.csv")

    def mostra_df(self):
        print(f"Anteprima Dataset:\n{self.df}")

    def mostra_info(self):
        print(f"Descrizione:\n{self.df.describe()}")
        print(f"Count valori:\n{self.df.count()}")

    def tipo_dati(self):
        #Verifico il tipo di dati
        print(self.df.dtypes)

    def verifica_valori_nulli(self):
        print(self.df.isnull().sum())

    def riempi_valori(self):
       # Sostituisce i valori mancanti con 0
        self.df.fillna(0, inplace=True)

    def correlazione(self):
        # Calcola la matrice di correlazione
        corr_matrix = self.df.corr()
        return corr_matrix

    def visualizza(self):
        corr_matrix = self.correlazione()
        plt.figure()
        sns.heatmap(corr_matrix)
        plt.title('Heatmap correlazione')
        plt.show()



a = Housing("Corso Python/Martedì 23/housing.csv")
a.mostra_info()
a.mostra_df()
a.verifica_valori_nulli()
a.visualizza()