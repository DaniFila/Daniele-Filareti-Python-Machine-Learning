import numpy as np

class LabScience:
    def __init__(self):
        self.temperature_per_ora = np.random.randint(0,40,24)

    def calcola_media(self):
        temp_media = np.mean(self.temperature_per_ora)
        print(f"La temperatura media di ogni ora è: {temp_media}")

    def find_max(self):
        max = np.max(self.temperature_per_ora)
        print(f"La temperatura massima è: {max}°")
    def find_min(self):
        min = np.min(self.temperature_per_ora)
        print(f"La temperatura minima è di: {min}°")

    def temperature_prossime_4_ore(self):
        incremento_giornaliero = 0.2/7 
        ultima_temp_reg = self.temperature_per_ora[-1]
        prox_temp = []
        for i in range(1,5):
            prox_temp.append(float(ultima_temp_reg + (i*incremento_giornaliero)))
        print(prox_temp)





def menu():
    info = """1: Visualizza temperature registrate:
2: Calcola media
3: Calcola Max
4: Calcola Min
5: Previsioni prossime 4 ore
0: Exit
"""
    s = input(info)
    return s
def main():
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