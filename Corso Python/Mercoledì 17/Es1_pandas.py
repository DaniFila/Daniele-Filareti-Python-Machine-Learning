import mod_Es1_pandas as Es1 # importo il modulo dell'esercizio con tutte le funzioni
def menu(): # funzione menù che stampa le opzioni e chiede all'utente la scelta
    info = """1: Visualizza DataFrame
2: Visualizza le prime 5 righe
3: Visualizza le ultime 5 righe
4: Visualizza il tipo di dati di ciascuna colonna
5: Calcola statistiche descrittive
6: Identificare e rimuovere eventuali duplicati
7: Gestione valori mancanti
8: Aggiunta Categoria età
9: Salva su file CSV
0: Exit
"""
    s = input(info)
    return s

def main(): # funzione main che richiama tutte le altre funzioni 
    df = Es1.genera_dataframe()
    while True:
        s = menu()
        if s == "1":
            print(df)
        elif s == "2":
            Es1.visualizza_prime_5_righe(df)
        elif s == "3":
            Es1.visualizza_ultime_5_righe(df)
        elif s == "4":
            Es1.visualizza_tipo_dati(df)
        elif s == "5":
            Es1.descrivi_stato(df)
        elif s == "6":
            Es1.rimuovi_duplicati(df)
        elif s == "7":
            Es1.gestione_valori_mancanti(df)
        elif s == "8":
            Es1.aggiungi_categorie_età_verifica(df)
        elif s == "9":
            Es1.salva_in_csv(df)
        elif s == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida!")


main()