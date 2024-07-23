import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Classe_Studenti:
    def __init__(self):
        self.df = self.crea_df()
    
    def crea_df(self):
        mesi = ['Mese1', 'Mese2', 'Mese3', 'Mese4', 'Mese5', 'Mese6']
        data = []
        for i in range(4):
            nome = input("Inserire Nome Studente: ")
            for mese in mesi:
                voto_italiano = float(input(f"Inserisci il voto di Italiano per {nome} in {mese}: "))
                voto_storia = float(input(f"Inserisci il voto di Storia per {nome} in {mese}: "))
                voto_inglese = float(input(f"Inserisci il voto di Inglese per {nome} in {mese}: "))
                voto_mate = float(input(f"Inserisci il voto di Matematica per {nome} in {mese}: "))
                data.append({
                    "Nome": nome,
                    "Mese": mese,
                    "Italiano": voto_italiano,
                    "Storia": voto_storia,
                    "Inglese": voto_inglese,
                    "Matematica": voto_mate})

        df = pd.DataFrame(data)
        return df
    
    def visualizza_stats(self):
        medie_df = self.df.groupby(["Nome","Mese"])[["Italiano","Storia","Inglese","Matematica"]].mean()
        medie_df["Media"] = medie_df.mean(axis=1)
        medie_df.reset_index(inplace=True)
        


a = Classe_Studenti()

print(a.df)

a.visualizza_stats()