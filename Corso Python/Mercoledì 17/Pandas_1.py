import pandas as pd

file_path = 'Corso Python/Mercoledì 17/vendite.csv'

df = pd.read_csv(file_path)

print(df.head())