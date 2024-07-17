import pandas as pd
import numpy as np

def genera_dataframe(): # funzione che genera un dataframe scegliendo dalle liste valori casuali di nomi e città e generando l'età e il salario
    nomi = ["Alessandro","Beatrice","Carlo","Daniele","Enrico","Francesca","Giulia","Leonardo","Martina","Nicola"]
    città =  ["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze","Venezia","Verona"]
    data = {"Nome":np.random.choice(nomi,20),
            "Città":np.random.choice(città,20),
            "Età":np.random.randint(0,90,20),
            "Salario":np.random.randint(1000,10000,20)}
    df = pd.DataFrame(data)
    return df

def visualizza_prime_5_righe(df): # funzione che visualizza le prime 5 righe del dataframe
    d = df.head()
    print(f"Le prime 5 righe sono:\n{d}")

def visualizza_ultime_5_righe(df): # funzione che visualizza le ultime 5 righe del dataframe
    d = df.tail()
    print(f"Le ultime 5 righe sono:\n{d}")

def visualizza_tipo_dati(df): # funzione che visualizza i tipi di dato nel dataframe
    tipo = df.dtypes
    print(f"I tipi di dati sono:\n{tipo}")

def descrivi_stato(df): # funzione che fa una serie di operazioni matematiche alle colonne età e salario
    descrivi = df.describe()
    print(f"Descrizione:\n{descrivi}")

def rimuovi_duplicati(df): # funzione che rimuove duplicati dal dataframe
    df_senza_duplicati = df.drop_duplicates()
    print("Eventuali valori duplicati eliminati!")
    return df_senza_duplicati

def salva_in_csv(df): # funzione che salva il dataframe su file CSV
    df.to_csv("Corso Python/Mercoledì 17/Es1.csv")
    print("Salvato con successo!")

def gestione_valori_mancanti(df): # funzione che gestisce i valori mancanti aggiungendo la mediana della colonna
    l = ["Età","Salario"]
    for i in l:
        df[i] = df[i].fillna(df[i].median())
    print(f"Eventuali valori mancanti gestiti!")

def categorie_età_verifica(età): # funzione che verifica l'età e restituisce la stringa corrispondente della categoria
    if età <= 18:
        return 'Giovane'
    elif età <= 65:
        return 'Adulto'
    else:
        return 'Senior'
    
def aggiungi_categorie_età_verifica(df): # funzione che richiama la funzione categorie_età_verifica e crea la colonna categorie età confrontando l'età e aggiungendo la categoria
    df["Categorie Età"] = df["Età"].apply(categorie_età_verifica)
    print("Categorie età aggiunta con successo!")





