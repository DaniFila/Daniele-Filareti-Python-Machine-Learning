import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay


class Case:
    def __init__(self):
        self.df = pd.read_csv("Corso Python/Giovedì 25/Real estate.csv")

    def regressione_lineare(self):
        X = self.df[["X2 house age","X3 distance to the nearest MRT station"]]
        y = self.df["Y house price of unit area"]

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
        model = LinearRegression()
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        print(f"Coefficiente: {model.coef_}")
        print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
        print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
        print(f"Predizioni:\n{y_pred}")
        display = PredictionErrorDisplay(y_true=y_test, y_pred=y_pred)
        display.plot()
        plt.show()



a = Case()
a.regressione_lineare()