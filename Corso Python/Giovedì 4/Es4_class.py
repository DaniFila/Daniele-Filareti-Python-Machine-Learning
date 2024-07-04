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
    def paga(tipo_pagamento,importo):
        try:
            tipo_pagamento.effettua_pagamento(importo)
            print("Successo!")
        except:
            print("Tipo di pagamento non valido!")


p = CartaDiCredito()

d = GestorePagamenti

d.paga(p,20)