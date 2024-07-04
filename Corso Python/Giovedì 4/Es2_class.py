class Posto:
    def __init__(self,numero,fila) -> None:
        self._numero = numero
        self._fila = fila
        self._occupato = False
    def prenota(self):
        if self._occupato:
            print("Il posto è già occupato")
        else:
            self._occupato = True
            print("Posto prenotato con successo")
    def libera(self):
        if self._occupato:
            self._occupato = False
            print("Posto liberato")
        else:
            print("Il posto risulta già libero")
    def stato(self):
        return self._occupato
    def get_fila(self):
        return self._fila
    def get_numero(self):
        return self._numero
    


class PostoVIP(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        self._accesso_lounge = False
        self._servizio_in_posto = False
    def prenota(self):
        if not self._occupato:
            a = input("Indicare servizio aggiuntivo:\n1:Accesso lounge\n2:Servizio al posto\nAltro per nessun servizio\n")
            if a == "1":
                self._accesso_lounge = True
                print("Servizio aggiunto!")
            elif a == "2":
                self._servizio_in_posto = True
                print("Servizio aggiunto!")
            else:
                print("Nessun servizio aggiunto")
        super().prenota()



class Teatro: 
    def __init__(self):
        self._posti = {} # dizionario con posti teatro
    def set_posti(self): # metodo per settare i posti nel teatro
        while True:
            fila = input("Indicare il nome della fila: ") # si richiede il nome della fila
            self._posti[fila] = [] # si crea come valore della fila una lista
            n_posti_fila = int(input("Indicare numero posti della fila: ")) # si indica il numero dei posti
            for posto in range(n_posti_fila):
                z = input("Il seguente posto è un posto vip:(si per accettare) ") # si richiede per ogni posto se è vip
                if z == "si": 
                    self._posti[fila].append(PostoVIP(posto,fila))
                else:
                    self._posti[fila].append(Posto(posto,fila))
            f = input("Vuoi aggiungere un'altra fila? (si per accettare): ") # si richiede se si vogliono aggiungere altre file
            if f != "si":
                break
    def prenota_posto(self,numero,fila): # metodo per prenotare posto
        if fila in self._posti:
            self._posti[fila][numero].prenota()
        else:
            print("Fila inesistente!")

    def stampa_posti_occupati(self): # metodo per stampare posto
        for fila in self._posti:
            for posto in self._posti[fila]:
                if posto.stato():
                    print(fila,posto.get_numero())
    


theater = Teatro()

theater.set_posti()
theater.prenota_posto(2,"uno")
theater.stampa_posti_occupati()