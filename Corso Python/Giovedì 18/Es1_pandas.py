import mod_Es1_pandas as Es1 # importo il modulo dell'esercizio

def menu(): # funzione menu che stampa menu e chiede all'utente la scelta
    info = """\n1: Visualizza DataFrame
2: Genera tabella Pivot
3: Applica Groupby
0: Exit
"""
    scelta = input(info)
    return scelta

def main(): # funzione main che richiama le altre funzioni
    df = Es1.DatiVendite()
    df.crea_df()
    while True:
        s = menu()
        if s == "1":
            print(f"\nDataframe:\n{df.df}")
        elif s == "2":
            df.tabella_pivot()
        elif s == "3":
            df.appl_groupby()
        elif s == "0":
            break
        else:
            print("\nScelta non valida")

main()