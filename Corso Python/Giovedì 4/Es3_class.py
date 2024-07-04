class Veicolo:
    def __init__(self):
        self.__marca = ""
        self.__modello = ""
        self.__anno = 0
        self.__accensione = False
    def accendi(self):
        if self.__accensione == False:
            self.__accensione = True
            print("Motore acceso!")
        else:
            print("Veicolo già in moto")
    def spegni(self):
        if self.__accensione:
            self.__accensione = False
            print("Motore spento!")
        else:
            print("Motore già non in moto")
    def __set_marca(self,marca):
        self.__marca = marca
    def __set_modello(self,modello):
        self.__modello = modello
    def __set_anno(self,anno):
        self.__anno = anno
    def __get_marca(self):
        return self.__marca
    def __get_modello(self):
        return self.__modello
    def __get_anno(self):
        return self.__anno
    



class GestoreParcoVeicoli(Veicolo):
    def __init__(self):
        Veicolo.__init__(self)
        self.__veicoli = []
    
    def aggiungi_veicolo(self,veicolo):
        veicolo._Veicolo__set_marca(input("Indicare Marca: "))
        veicolo._Veicolo__set_modello(input("Indicare Modello: "))
        veicolo._Veicolo__set_anno(int(input("Indicare anno: ")))
        self.__veicoli.append(veicolo)

    def rimuovi_veicolo(self,marca,modello):
        found = False
        for veicolo in self.__veicoli:
            marcas = veicolo._Veicolo__get_marca()
            modellos = veicolo._Veicolo__get_modello()
            if marca == marcas and modello == modellos:
                self.__veicoli.remove(veicolo)
                print("Veicolo rimosso con successo!")
                found = True
        if not found:
            print("Veicolo non presente")
    
    def lista_veicoli(self):
        for veicolo in self.__veicoli:
            print(f"Marca: {veicolo._Veicolo__get_marca()}, Modello: {veicolo._Veicolo__get_modello()}, Anno: {veicolo._Veicolo__get_anno()}")




v = Veicolo()


# v1 = Veicolo()

a = GestoreParcoVeicoli()

a.aggiungi_veicolo(v)
# a.aggiungi_veicolo(v1)
# a.rimuovi_veicolo("Ferrari","Roma")
a.lista_veicoli()
