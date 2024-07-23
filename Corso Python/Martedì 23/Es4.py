import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Classe_Studenti:
    def __init__(self):
        self.df = self.dataframe_demo()
    
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
    
    def dataframe_demo(self):
        data=[]
        mesi = ['Mese1', 'Mese2', 'Mese3', 'Mese4', 'Mese5', 'Mese6']
        studenti = ["Peppino","Antonio"]
        for nome in studenti:
            for mese in mesi:
                voto_ita = np.random.randint(1,11)
                voto_stor = np.random.randint(1,11)
                voto_mate = np.random.randint(1,11)
                voto_ingl = np.random.randint(1,11)
                data.append({"Nome":nome,"Mese":mese,"Italiano":voto_ita,"Storia":voto_stor,"Inglese":voto_ingl,"Matematica":voto_mate})
        df = pd.DataFrame(data)
        return df

    def calcola_stats(self):
        medie_df = self.df.groupby(["Nome","Mese"])[["Italiano","Storia","Inglese","Matematica"]].mean()
        medie_df["Media"] = medie_df.mean(axis=1)
        medie_df.reset_index(inplace=True)
        
        stud1_df = medie_df.loc[medie_df["Nome"] == "Peppino"]
        stud2_df = medie_df.loc[medie_df["Nome"] == "Antonio"]
        stud2_df.reset_index(inplace=True)
        stud1_df.reset_index(inplace=True)

        return stud1_df,stud2_df
    
    def visualizza_stats_subplot(self):
        stud1_df,stud2_df = self.calcola_stats()
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(stud1_df["Media"])
        plt.title("Media dell'alunno Peppino")
        plt.subplot(2,1,2)
        plt.plot(stud2_df["Media"])
        plt.title("Media dell'alunno Antonio")
        plt.show()
        


a = Classe_Studenti()

print(a.df)

a.visualizza_stats()