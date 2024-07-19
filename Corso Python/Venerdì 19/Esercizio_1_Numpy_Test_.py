import numpy as np

class LabScience:
    def __init__(self): # metodo costruttore dove creo un array con valori casuali che indicano i graid
        self.temperature_per_ora = np.random.randint(0,40,24)

    def calcola_media(self): # metodo per calcolare la temperatura media 
        temp_media = np.mean(self.temperature_per_ora)
        print(f"La temperatura media di ogni ora è: {temp_media}")

    def find_max(self): # metodi per visualizzare la temperatura massima e la minima
        max = np.max(self.temperature_per_ora)
        print(f"La temperatura massima è: {max}°")
    def find_min(self):
        min = np.min(self.temperature_per_ora)
        print(f"La temperatura minima è di: {min}°")

    def temperature_prossime_4_ore(self): # metodo per visualizzare le temperature previste per le prossime 4 ore
        incremento_giornaliero = 0.2/7  # faccio un calcolo dell'incremento diviso 7 che sono i giorni della settimana
        ultima_temp_reg = self.temperature_per_ora[-1] # mi salvo l'ultima temperatura registrata
        prox_temp = [] # mi creo una lista dove inserirò le temperature future previste
        for i in range(1,5): # faccio un range da 1 a 4 che sono le ore
            prox_temp.append(float(ultima_temp_reg + (i*incremento_giornaliero))) # faccio una moltiplicazione tra l'orario e l'incremento giornaliero e lo sommo all'ultima temperatura registrata e lo aggiungo alla lista
        print(prox_temp) # stampo il risultato





def menu(): # funzione menu che stampa un menu e le opzioni che si possono fare
    info = """1: Visualizza temperature registrate:
2: Calcola media
3: Calcola Max
4: Calcola Min
5: Previsioni prossime 4 ore
0: Exit
"""
    s = input(info)
    return s
def main(): # funzione main che richiama le altre
    reg = LabScience()
    while True:
        s = menu()
        if s == "1":
            print(reg.temperature_per_ora)
        elif s == "2":
            reg.calcola_media()
        elif s == "3":
            reg.find_max()
        elif s == "4":
            reg.find_min()
        elif s == "5":
            reg.temperature_prossime_4_ore()
        elif s == "0":
            break
        else:
            print("Error")


main()