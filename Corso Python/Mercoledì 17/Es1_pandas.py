import pandas as pd
import numpy as np


def genera_dataframe():
    nomi = ["Alessandro","Beatrice","Carlo","Daniela","Enrico","Francesca","Giulia","Leonardo","Martina","Nicola"]
    città =  ["Roma","Milano","Napoli","Torino","Palermo","Genova","Bologna","Firenze","Venezia","Verona"]
    data = {"Nome":np.random.choice(nomi,20),
            "Città":np.random.choice(città,20),
            "Età":np.random.randint(0,90,20),
            "Salario":np.random.randint(1000,10000,20)}
    df = pd.DataFrame(data)
    return df





