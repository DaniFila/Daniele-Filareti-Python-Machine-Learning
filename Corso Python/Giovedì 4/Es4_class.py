class MetodoPagamento:
    def effettua_pagamento(self,importo):
        print("Elaborazione...")

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        print("Transazione eseguita con Carta di Credito!")
    
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        print(f"Pagamento di {importo} eseguito correttamente!")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        iban = input("Inserisci iban: ")
        print(f"Pagamento tramite Bonifico di {importo} su iban: {iban},eseguito correttamente!")

class GestorePagamenti:
    def paga(self,tipo_pagamento,importo):
        try:
            tipo_pagamento.effettua_pagamento(importo)
            print("Successo!")
        except:
            print("Tipo di pagamento non valido!")

class Menu():
    def pagamento(self):
        while True:
            a = input("Indicare metodo di pagamento:\n1: Carta di Credito\n2: PayPal\n3: Bonifico Bancario\n")
            if a == "1":
                z = CartaDiCredito()
                break
            elif a == "2":
                z = PayPal()
                break
            elif a == "3":
                z = BonificoBancario()
                break
            else:
                print("Error")
        importo = int(input("Indicare importo: "))
        gestione = GestorePagamenti()
        gestione.paga(z,importo)
            

a = Menu()
a.pagamento()