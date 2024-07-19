import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Corso Python/Venerdì 19/Esercizio_2_Pandas_Test.csv")

def grafico_barre():
    # Creare un grafico a barre
    sns.barplot(x="Data", y="Vendite", data=df)
    plt.title('Conto Totale per Giorno')
    plt.show()

def grafico_linee():
    # Creare un grafico a linee
    sns.lineplot(x="Data", y="Vendite", data=df, hue="Filiare")
    plt.title('Segnale FMRI nel Tempo')
    plt.show()

def istogramma_kde():
    # Creare un istogramma con KDE
    sns.histplot(data=df, x="Vendite", kde=True)
    plt.title('Distribuzione Vendite')
    plt.show()

