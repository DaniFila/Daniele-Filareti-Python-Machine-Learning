import pandas as pd

data = {"nome": ["Alice","Bob"],"Età":[25,30]}
df = pd.DataFrame(data)

df.to_csv("Corso Python/Giovedì 18/pandas_creazione_caricamento.csv")

df_csv = pd.read_csv("Corso Python/Giovedì 18/pandas_creazione_caricamento.csv")

