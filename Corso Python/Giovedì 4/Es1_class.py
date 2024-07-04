class ContoBancario:
    def __init__(self):
        self.__titolare = "" # attributo privato __
        self.__saldo = 0 # attributo privato __
    def deposita(self,importo): # metodo per depositare importo dato nel metodo
        if importo > 0:
            self.__saldo += importo
        else:
            print("Importo non valido")
    def preleva(self,importo): # metodo per prelevare importo indicato nell'inserimento del metodo
        if self.__saldo >= importo:
            self.__saldo -= importo
            print("Prelievo completato")
        else:
            print("Saldo non disponibile")
    def visualizza_saldo(self): # metodo per visualizzare attributo privato saldo
        return self.__saldo
    
    def set_titolare(self): # metodo per impostare nome titolare
        a = input("Inserire nome del titolare: ")
        if a != "":
            self.__titolare = a
            print("Nome impostato correttamente!")
        else:
            print("Non valido")
    def get_titolare(self): # metodo per avere il nome del titolare
        return self.__titolare
    
    def set_saldo(self): # metodo per impostare il saldo
        a = int(input("Inserire saldo: "))
        if a >0:
            self.__saldo = a
            print("Saldo impostato correttamente")
        else:
            print("Valore non valido")

    

