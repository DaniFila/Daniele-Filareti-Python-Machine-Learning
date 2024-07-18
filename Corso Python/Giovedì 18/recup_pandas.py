import pandas as pd
# Creazione di un DataFrame da un dizionario
data = {"nome": ["Alice","Bob"],"Età":[25,30]}
df = pd.DataFrame(data)
# Caricamento di un DataFrame da un file CSV
df.to_csv("Corso Python/Giovedì 18/pandas_creazione_caricamento.csv")

df_csv = pd.read_csv("Corso Python/Giovedì 18/pandas_creazione_caricamento.csv")

#--------------------------------------------------------------------------------------------------------------------------
# Visualizzazione delle statistiche descrittive
print(df.describe())

# Rimozione dei valori mancanti
df_clean = df.dropna()

#--------------------------------------------------------------------------------------------------------------------------

# Selezione di una colonna
ages = df['età']

# Filtraggio basato su una condizione
adults = df[df['età'] >= 18]

#--------------------------------------------------------------------------------------------------------------------------

# Ordinamento dei dati per età
df_sorted = df.sort_values(by='età')

# Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')