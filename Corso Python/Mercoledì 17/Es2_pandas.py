import mod_Es2_pandas as Es2

def scelte_menu(): # funzione menù che stampa le opzioni e chiede all'utente la scelta
        info = """\n1: Visualizza DataFrame
2: Aggiungi colonna Totale Vendite
3: Raggruppa i dati per Prodotto e calcola il totale delle vendite per ciascun prodotto
4: Trova il prodotto più venduto in termini di Quantità
5: Identifica la città con il maggior volume di vendite totali
6: Crea un nuovo DataFrame che mostri solo le vendite superiori a un certo valore
7: Ordina il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente
8: Visualizza il numero di vendite per ogni città
0: Exit
"""
        scelta = input(info)
        return scelta
    

def main(): # funzione main che richiama la classe menù e la classe Vendite del modulo Es2
    df = Es2.Vendite()
    df.genera_dataframe()
    while True:
        scelta = scelte_menu()
        if scelta == "1":
            print(f"DataFrame:\n{df.df}")
        elif scelta == "2":
            df.aggiungi_totale_vendite()
        elif scelta == "3":
            try:
                df.raggruppa_vendite_per_prodotto()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "4":
            try:  # verifica per l'operazione che la colonna Vendite Totali sia creata
                df.prodotto_più_venduto_su_quantità()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "5":
            try: # verifica per l'operazione che la colonna Vendite Totali sia creata
                df.città_con_maggior_volume_vendite_tot()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "6":
            try: # verifica per l'operazione che la colonna Vendite Totali sia creata
                df.nuovo_dataframe_filtrato()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "7":
            try: # verifica per l'operazione che la colonna Vendite Totali sia creata
                df.ordina_tot_vendite_desc()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "8":
            try: # verifica per l'operazione che la colonna Vendite Totali sia creata
                df.visualizza_vendite_per_città()
            except:
                print("\nColonna Vendite Totali non creata!")
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida")


main()