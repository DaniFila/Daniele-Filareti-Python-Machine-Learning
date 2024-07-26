import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay

class Banca:
    scala_lavori = {"unemployed":0,"student":0,"services":1,"technician":1,"blue-collar":1,"housemaid":1,"entrepreneur":2,"self-employed":2,"retired":2,"admin":3,"management":3}
    scala_coniugale = {"divorced":0,"single":2,"married":1}

    def __init__(self):
        self.df = pd.read_csv("Corso Python/Venerdì 26/Es1_Regress_Logist.csv")

    def prep_predict(self):
        self.df["job"] = self.df["job"].loc[self.df["job"] != "unknown"]
        self.df["job"] = self.df["job"].map(self.scala_lavori)

        self.df["marital"] = self.df["marital"].loc[self.df["marital"] != "unknown"]
        self.df["marital"] = self.df["marital"].map(self.scala_coniugale)

        self.df["default"] = self.df["default"].loc[self.df["default"] != "unknown"]
        self.df["default"] = self.df["default"].map({"no":0,"yes":1})

        self.df["housing"] = self.df["housing"].loc[self.df["housing"] != "unknown"]
        self.df["housing"] = self.df["housing"].map({"no":0,"yes":1})

        self.df["loan"] = self.df["loan"].loc[self.df["loan"] != "unknown"]
        self.df["loan"] = self.df["loan"].map({"no":0,"yes":1})

        self.df.dropna(inplace=True)


    def regressione_logistica(self):
        X = self.df[["age","job","marital","default","housing","loan","emp_var_rate","cons_conf_idx","previous","campaign","euribor3m","cons_price_idx"]]
        y = self.df["y"]

        X_train,X_test,y_train,y_test = train_test_split(X,y)
        model = LogisticRegression(random_state=0,solver='liblinear',C=100.0)
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)

        print(f"Score: {model.score(X_train,y_train)}")
        print(f"Report: {classification_report(y_train,model.predict(X_train))}")
        cm = confusion_matrix(y_train, model.predict(X_train))
        print(f"1:{cm}")
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(cm)
        ax.grid(False)
        ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
        ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
        ax.set_ylim(1.5, -0.5)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
        plt.show()

        cm = confusion_matrix(y_test, y_pred)
        print(f"2:{cm}")
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(cm)
        ax.grid(False)
        ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
        ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
        ax.set_ylim(1.5, -0.5)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
        plt.show()

        
a = Banca()
a.prep_predict()

a.regressione_logistica()