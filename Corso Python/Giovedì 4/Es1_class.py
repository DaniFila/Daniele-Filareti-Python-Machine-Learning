class ContoBancario:
    def __init__(self):
        self.__titolare = ""
        self.__saldo = 0
    def deposita(self,importo):
        if importo > 0:
            self.__saldo += importo
        else:
            print("Importo non valido")
    def preleva(self,importo):
        if self.__saldo >= importo:
            self.__saldo -= importo
            print("Prelievo completato")
        else:
            print("Saldo non disponibile")
    def visualizza_saldo(self):
        return self.__saldo
    
    def set_titolare(self):
        a = input("Inserire nome del titolare: ")
        if a != "":
            self.__titolare = a
            print("Nome impostato correttamente!")
        else:
            print("Non valido")
    def get_titolare(self):
        return self.__titolare
    
    def set_saldo(self):
        a = int(input("Inserire saldo: "))
        if a >0:
            self.__saldo = a
            print("Saldo impostato correttamente")
        else:
            print("Valore non valido")

    

