import pandas as pd


class CatenaRistoranti:
    def __init__(self,nome_file):
        try:
            self.df = pd.read_csv(nome_file) # col percorso legge il file csv e lo salva in un DataFrame
            self.nome_file = nome_file
            print(f"\nFile: {nome_file} Caricato con successo!")
        except FileNotFoundError:
            print(f"\nFile: {nome_file} non trovato!")
        except:
            print("\nErrore, non è stato possibile caricare il File!")
    
    def save_csv(self,nome_file): # metodo che salva il DataFrame in csv
        try:
            self.df.to_csv(nome_file,index=False)
            print(f"\nFile: {nome_file} Salvato con successo!")
        except:
            print(f"\nErrore: il file {nome_file} non è stato salvato!")

    def groupby(self):
        raggruppa_per_filiare = self.df.groupby("Filiare").agg({"Vendite":"sum"})
        raggruppa_per_data = self.df.groupby("Data").agg({"Vendite":"sum"})
        print(f"\nEcco i raggruppamenti per data e per filiare:\n{raggruppa_per_data}\n{raggruppa_per_filiare}")
        raggruppa_per_filiare.to_csv("Groupby_filiare.csv") 
        raggruppa_per_data.to_csv("Groupby_data.csv")   
    
    def media_vendite_giornaliere(self):
        raggruppa_per_data = self.df.groupby(["Data","Filiare"]).agg({"Vendite":"mean"})
        raggruppa_per_data.groupby(["Filiare","Vendite"]).mean()
        print(f"\nMedia vendite giornaliere:\n{raggruppa_per_data}")
        raggruppa_per_data.to_csv("Media_vendite.csv")

    def filiare_venduto_di_più(self):
        filiare_max = self.df.groupby("Filiare").agg({"Vendite":"sum"}).idxmax()
        print(f"La filiare che ha venduto di più è stata:\n{filiare_max}")
        filiare_max.to_csv("Filiare_max_vendite.csv")





def menu():
    info = """1: Visualizza DataSet
2: Visualizza raggruppamenti
3: Visualizza media vendite giornaliere
4: Visualizza la filiare che ha venduto di più
0: Exit
"""
    s = input(info)
    return s

def main():
    a = CatenaRistoranti("Corso Python/Venerdì 19/Esercizio_2_Pandas_Test.csv")
    while True:
        s = menu()
        if s == "1":
            print(f"Dataset\n{a.df}")
        elif s == "2":
            a.groupby()
        elif s == "3":
            a.media_vendite_giornaliere()
        elif s == "4":
            a.filiare_venduto_di_più()
        elif s == "0":
            break
        else:
            print("Error")


main()