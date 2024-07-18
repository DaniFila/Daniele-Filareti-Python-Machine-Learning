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
ages = df['Età']

# Filtraggio basato su una condizione
adults = df[df['Età'] >= 18]

#--------------------------------------------------------------------------------------------------------------------------

# Ordinamento dei dati per età
df_sorted = df.sort_values(by='Età')

# Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')

#--------------------------------------------------------------------------------------------------------------------------

# Applicazione di una funzione a una colonna
df['età_doppia'] = df['Età'].apply(lambda x: x * 2)

#--------------------------------------------------------------------------------------------------------------------------

# Ordinamento dei dati per età
df_sorted = df.sort_values(by='Età')

# Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')

#--------------------------------------------------------------------------------------------------------------------------

# Applicazione di una funzione a una colonna
df['età_doppia'] = df['Età'].apply(lambda x: x * 2)

#--------------------------------------------------------------------------------------------------------------------------

# Esportazione di un DataFrame in un file CSV
#df.to_csv('"Corso Python/Giovedì 18/pandas_creazione_caricamento.csv')

#--------------------------------------------------------------------------------------------------------------------------

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()

#--------------------------------------------------------------------------------------------------------------------------
