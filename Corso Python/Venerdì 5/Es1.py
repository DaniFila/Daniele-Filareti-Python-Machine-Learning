import random

class GestioneClienti:
     
    clienti={}

    def crea_clienti(self,cliente):
        cliente._ContoBancario__set_nome(input("inserisci il nome: "))
        cliente._ContoBancario__set_cognome(input("inserisci il cognome: "))
        cliente._ContoBancario__set_saldo(int(input("inserisci il saldo iniziale: ")))
        self.clienti[cliente._ContoBancario__get_numero_conto()] = cliente


    def elimina_cliente(self,conto):
        trovato = False
        for n_conto,cliente in self.clienti.items():
            if cliente == conto:
                i = n_conto
                trovato = True
        if trovato:
            self.clienti.pop(i)
            print("Eliminato!")
        else:
            print("Cliente non trovato")
                


    def modifica_cliente(self,conto):
        trovato = False
        for n_conto,cliente in self.clienti.items():
            if cliente == conto:
                i = n_conto
                trovato = True
        if trovato:
            while True:
                a = input("Indica azione:\n1: Modifica Nome\n2: Modifica Cognome\n3: Exit\n")
                if a == "1":
                    conto._ContoBancario__set_nome(input("inserisci il nome: "))
                elif a == "2":
                    conto._ContoBancario__set_cognome(input("inserisci il cognome: "))
                elif a == "3":
                    break
                else:
                    print("Error")
            self.clienti[i] = conto
            print("Modificato con successo!")
        else:
            print("Conto non trovato")


    



    
        


        
class ContoBancario:

    def __init__(self):
        self.__saldo=0

        self.__nome=""
        self.__cognome=""
        self.__numero_conto= ''.join(str(random.randint(0, 9)) for _ in range(13))

    def __set_nome(self,nome):
         self.__nome=nome

    def __set_cognome(self,cognome):
         self.__cognome=cognome

    def __set_saldo(self,saldo):
         self.__saldo=saldo

   

    def get_nome(self):
        return self.__nome
    
    def get_cognome(self):
        return self.__cognome
    
    def __get_numero_conto(self):
            return self.__numero_conto
    
    def visualizza_dettagli_cliente(self):
        print(f"Nome: {self.__nome}  {self.__cognome}")
        print(f"Numero conto: {self.__numero_conto}")
        
    def deposita(self,importo):
        if importo>0:
            self.__saldo=self.__saldo+importo
        else:
            return f"Importo insufficiente"
        
    def preleva(self,importo):
        if self.__saldo>=importo and importo>0:
            self.__saldo=self.__saldo-importo
        else:
            return f"Saldo insufficiente"
        
    def visualizza_saldo(self):
        print(f"Saldo disponibile: {self.__saldo}")

    
    def get_saldo(self):
        return self.__saldo
    
    def effettua_pagamento(self, importo, beneficiario):
        if self.__saldo >= importo and importo > 0:
            self.__saldo -= importo
            beneficiario.deposita(importo)
            print(f"Pagamento di {importo} effettuato a favore di {beneficiario.get_nome()} {beneficiario.get_cognome()}.")
        else:
            return "Saldo insufficiente o importo non valido"
              


cliente=ContoBancario()
cliente2 = ContoBancario()
gestione=GestioneClienti()
gestione.crea_clienti(cliente)
print(gestione.clienti)
gestione.modifica_cliente(cliente)
print(gestione.clienti)
cliente.visualizza_dettagli_cliente()
cliente.visualizza_saldo()

cliente.effettua_pagamento(200, cliente2)