import pandas as pd

data = {"Nome":["Daniele","Aurora"],
        "Età":[21,18],
        "Città":["Castelnovo Ne' Monti","Cariati"],
        "Sesso":["Maschio","Femmina"]}

df = pd.DataFrame(data)

print(f"Il dataframe creato è:\n{df}")


df_older = df[df["Età"]>18]

print(f"Persone con età superiore a 18:\n{df_older}")

df["Maggiorenne"] = df["Età"] >=18


print(f"Dataframe aggiornato:\n{df}")
