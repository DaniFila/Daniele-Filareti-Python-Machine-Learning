from random import randint

class Libro:
    def __init__(self,titolo,autore,prezzo,isbn,stato_prestito):
        self.__titolo = titolo
        self.__autore = autore
        self.prezzo = prezzo
        self.__isbn = isbn
        self.stato_prestito = stato_prestito

    def __str__(self):
        return f"Il titolo del libro è: {self.__titolo}, l'autore è: {self.__autore}, il prezzo è: {self.prezzo},il codice isbn è: {self.__isbn}, lo stato del prestito è: {self.stato_prestito}"
    def applica_sconto(self):
        sconto = input("Indicare sconto: ")
        while not sconto.isalnum:
            sconto = input("indicare sconto corretto: ")
        sconto_i = int(sconto)/100
        self.prezzo = self.prezzo*sconto_i
    def prestito(self):
        if self.stato_prestito == "Disponibile":
            self.stato_prestito = "In prestito"
            print("Libro prestato")
        else:
            self.stato_prestito = "Disponibile"
            print("Libro di nuovo disponibile")
    def isbn(self):
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "1234567890"
        isbn = ""
        for i in range(2):
            isbn+=alfabeto[randint(0,25)]
            isbn+=num[randint(0,9)]
        self.__isbn = isbn


def isbn():
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    isbn = ""
    for i in range(2):
        print(alfabeto[randint(0,25)])
        isbn+=alfabeto[randint(0,25)]
        isbn+=num[randint(0,9)]
    return isbn

a = isbn()


libro1 = Libro("Pirati","Tizio",45,a,"Disponibile")

print(libro1)

libro1.applica_sconto()

print(libro1)

libro1.prestito()

print(libro1)