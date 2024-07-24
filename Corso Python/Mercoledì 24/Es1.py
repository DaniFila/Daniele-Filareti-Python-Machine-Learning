import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
class Netflix:
    def __init__(self,nome_file):
        self.df = pd.read_csv(nome_file)
    
    def verifica_valori_nulli(self):
        print(f"Elenco valori nulli:\n{self.df.isnull().sum()}")

    def scrivi_df(self):
        self.df.to_csv("Corso Python/Martedì 23/netflix_titles_pulito.csv")
        print("\nFile salvato con successo!")


    def pulizia(self):
        """self.df["rating"].fillna("G",inplace=True)
        self.df["duration"].fillna("Not Defined",inplace=True)"""
        self.df.loc[self.df["rating"].isnull()] = "G"
        self.df.loc[self.df["duration"].isnull()] = "Not Defined"
        self.df.dropna(inplace=True)
        print("\nIl Dataset è stato pulito con successo!")

    def df_movie(self):
        df_movie_ = self.df.loc[self.df["type"] == "Movie"] 
        return df_movie_
    def df_series(self):
        df_series_ = self.df.loc[self.df["type"] == "TV Show"]
        return df_series_
    
    def visualizza_df(self):
        print(f"DataSet:\n{self.df}")

    def prep_corr_rating(self):
        rating = self.df["rating"]
        rating.drop_duplicates(inplace=True)
        print(rating)
    """def sost_rating(self,rat):
        dizionario = {"PG-13":1,"TV-MA":2,"PG":3,"TV-14":4,"TV-PG":5,"TV-Y":6,"TV-Y7":7,"R":8}"""
    def preprazione_correlazione(self):
        self.df['type'] = self.df['type'].apply(lambda x: 1 if x == 'Movie' else 0)
        """type = self.df["type"]
        anno_uscita = self.df["release_year"]
        data = {"type":type,"release_year":anno_uscita}"""
        df_corr = self.df[["type","release_year"]]
        #df_corr = pd.DataFrame(data)
        df_corr = df_corr.corr()
        return df_corr
    def visualizza_correlazione(self):
        df_corr = self.preprazione_correlazione()
        plt.figure()
        sns.heatmap(df_corr,annot=True)
        plt.title('Heatmap correlazione')
        plt.show()

    def grafico_film_serie_a_torta(self):
        df_type = self.df["type"]
        film = df_type[self.df["type"] == "Movie"].count()
        serie = df_type[self.df["type"]== "TV Show"].count()
        totale = film+serie
        film_perc  = (film*100) / totale
        serie_perc = (serie*100) / totale
        x = [film_perc,serie_perc]
        label = ["Film","Serie TV"]
        plt.pie(x,labels=label,autopct='%.1f')
        plt.title("Grafico Film e Serie TV")
        plt.show()

    def grafico_andamento_tempo_prodotti(self):
        df_stat = self.df[["type","release_year"]]
        film = df_stat[self.df["type"] == "Movie"]
        serie = df_stat[self.df["type"]== "TV Show"]
        film_group = film.groupby("release_year").count()
        serie_group = serie.groupby("release_year").count()
        plt.figure()
        plt.plot(film_group)
        plt.plot(serie_group)
        plt.title("Andamento nel tempo produzione Film/Serie TV")
        plt.legend(["Film","Serie TV"])
        plt.show()

    def grafico_distribuzioni_paesi(self):
        self.pulizia()
        df_country = self.df[["type","country"]]
        df_country["country"] = df_country["country"].apply(lambda x: x.split(',')[0].strip())
        df_country_group = df_country.groupby("country").size().sort_values(ascending=False).head(20)
        plt.figure(figsize=(10, 6))
        df_country_group.plot(kind='bar', color='skyblue')
        plt.title('Numero di Film Prodotti per Nazione')
        plt.xlabel('Nazione')
        plt.ylabel('Numero di Film')
        plt.show()
        



def menu():
    info = """\n1  Visualizza anteprima DataSet
2: Visualizza Elenco Valori nulli
3: Pulisci DataSet
4: Visualizza possibili Correlazioni
5: Salva DataSet aggiornato
6: Visualizza Grafico a Torta Film/Serie TV
7: Visualizza Andamento produzione Film/Serie TV
0: Exit
Indicare la scelta: """
    s = input(info)
    return s

def main():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    a = Netflix("Corso Python/Martedì 23/netflix_titles.csv")
    while True:
        s = menu()
        if s == "1":
            a.visualizza_df()
        elif s == "2":
            a.verifica_valori_nulli()
        elif s == "3":
            a.pulizia()
        elif s == "4":
            a.visualizza_correlazione()
        elif s == "5":
            a.scrivi_df()
        elif s == "6":
            a.grafico_film_serie_a_torta()
        elif s == "7":
            a.grafico_andamento_tempo_prodotti()
        elif s == "0":
            a.grafico_distribuzioni_paesi()
            break
        else:
            print("\nScelta non valida!")

main()
