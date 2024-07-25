import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class Calorie:
    def __init__(self):
        self.df = self.leggi_df()
    
    def leggi_df(self):
        df = pd.read_csv("Corso Python/Giovedì 25/calorie.csv")
        return df
    def regressione_lineare(self):
        X = self.df[["kg"]]
        y = self.df["calories"]
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
        modello = LinearRegression()
        modello.fit(X_train,y_train)
        y_pred = modello.predict(X_test)
        print(f"Coefficiente: {modello.coef_}")
        print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
        print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
        plt.scatter(X_test, y_test)
        plt.plot(X_test,y_pred)

        plt.xticks(())
        plt.yticks(())

        plt.show()

        


a = Calorie()
a.regressione_lineare()