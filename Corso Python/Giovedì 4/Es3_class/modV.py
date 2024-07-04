class Veicolo: # classe Veicolo
    def __init__(self): # nel costruttore dichiaro tutti gli attributi privati
        self.__marca = ""
        self.__modello = ""
        self.__anno = 0
        self.__accensione = False
    def accendi(self): # metodo per accendere il motore se spento e cambio attributo privato accensione
        if self.__accensione == False:
            self.__accensione = True
            print("Motore acceso!")
        else:
            print("Veicolo già in moto")
    def spegni(self): # metodo per spegnere il motore se acceso e cambio attributo privato accensione
        if self.__accensione:
            self.__accensione = False
            print("Motore spento!")
        else:
            print("Motore già non in moto")
    def __set_marca(self,marca): # metodo privato per impostare marca
        self.__marca = marca
    def __set_modello(self,modello): # metodo privato per impostare modello
        self.__modello = modello
    def __set_anno(self,anno): # metodo privato per impostare anno
        self.__anno = anno
    def __get_marca(self): # metodo privato per ricevere attributo privato marca
        return self.__marca 
    def __get_modello(self): # metodo privato per ricevere attributo privato modello
        return self.__modello
    def __get_anno(self): # metodo privato per ricevere attributo privato anno
        return self.__anno
    

class Auto(Veicolo): # classe derivata di Veicolo
    def __init__(self):
        Veicolo.__init__(self) # eredita attributi e metodi di Veicolo
        self.__numero_porte = 0  # attributo privato del numero porte
    def suona_clacson(self): # metodo che stampa un'ipotetico suono del clacson 😅
        print("TU TUUUUUU")
    def set_numero_porte(self,numero): # metodo per impostare attributo privato del numero porte
        self.__numero_porte = numero
    def get_numero_porte(self): # metodo per ricevere il valore dell'attributo privato del numero porte
        return self.__numero_porte
    
class Furgone(Veicolo): # classe derivata di Veicolo
    def __init__(self):
        Veicolo.__init__(self) # eredita attributi e metodi di Veicolo
        self.__capacità_carico = 0 # attributo privato della capacità di carico
    def carica(self): # metodo per incrementare capacità carico
        self.__capacità_carico +=1
    def scarica(self): # metodo per decrementare capacità carico
        self.__capacità_carico -=1
    def set_carico(self,numero): # metodo per impostare attributo privato carico
        self.__capacità_carico = numero
    def get_carico(self): # metodo per ricevere attributo privato carico
        return self.__capacità_carico
    
class Motocicletta(Veicolo): # classe derivata di Veicolo
    def __init__(self):
        Veicolo.__init__(self) # eredita attributi e metodi di Veicolo
        self.__tipologia = "" # attributo privato tipologia della motocicletta
    def set_tipo(self,type): # metodo per impostare attributo privato della tipologia 
        self.__tipologia = type
    def get_tipo(self): # metodo per ricevere attributo privato della tipologia
        return self.__tipologia
    def esegui_wheelie(self): # metodo per eseguire wheelie solo se il tipo è sportivo
        if self.__tipologia == "sportivo":
            print("Eseguito!")
        else:
            print("Non adatto")




class GestoreParcoVeicoli(Veicolo): # classe di gestione che eredita attributi e metodi della classe Veicolo
    def __init__(self):
        Veicolo.__init__(self)
        self.__veicoli = [] # attributo privato lista veicoli
    
    def aggiungi_veicolo(self,veicolo): # metodo per aggiungere veicolo alla lista privata dei veicoli
        veicolo._Veicolo__set_marca(input("Indicare Marca: ")) # si richiama il metodo privato della classe Veicolo per l'oggetto Veicolo 
        veicolo._Veicolo__set_modello(input("Indicare Modello: ")) # si richiama il metodo privato della classe Veicolo per l'oggetto Veicolo
        veicolo._Veicolo__set_anno(int(input("Indicare anno: "))) # si richiama il metodo privato della classe Veicolo per l'oggetto Veicolo
        self.__veicoli.append(veicolo) # aggiunge il veicolo alla lista

    def rimuovi_veicolo(self,marca,modello): # metodo per rimuovere veicolo ricercando tramite marca e modello
        found = False # booleano per tracciare se è stato trovato
        if self.__veicoli == []: # verifica che la lista non sia vuota, eventualmente stampa un messaggio
            print("Non ci sono veicoli nel Parco!")
        else:
            for veicolo in self.__veicoli: # si scannerizza la lista dei veicoli
                marcas = veicolo._Veicolo__get_marca() # si ricava dall'attributo privato della classe Veicolo la marca
                modellos = veicolo._Veicolo__get_modello() # si ricava dall'attributo privato della classe Veicolo il modello
                if marca == marcas and modello == modellos: # se marca e modello corrispondono con il veicolo scannerizzato 
                    self.__veicoli.remove(veicolo) # si rimuove il veicolo dalla lista
                    print("Veicolo rimosso con successo!") # stampa un messaggio di avvenuta rimozione
                    found = True # si imposta il booleano su True 
            if not found: # se non è stata trovata corrispondenza
                print("Veicolo non presente") # stampa avviso
    
    def lista_veicoli(self): # metodo per stampare veicoli in lista formattati con marca,modello e anno
        if self.__veicoli == []: # verifica che la lista non sia vuota, eventualmente stampa un messaggio
            print("Non ci sono veicoli nel Parco!")
        else:
            for veicolo in self.__veicoli:
                print(f"Marca: {veicolo._Veicolo__get_marca()}, Modello: {veicolo._Veicolo__get_modello()}, Anno: {veicolo._Veicolo__get_anno()}")
    
    def gestore(self,veicolo): # metodo per gestire un veicolo passato insieme al metodo
        while True:
            selezione = input("Indicare operazioni:\n1: set marca\n2: set modello\n3: set anno\n4: get marca\n5: get modello\n6: get anno\n7: Exit\n")
            if selezione == "1": # se si indica 1 allora si richiama il metodo privato della classe Veicolo e si richiede di impostare la marca
                veicolo._Veicolo__set_marca(input("Indicare Marca: "))
            elif selezione == "2": # se si indica 2 allora si richiama il metodo privato della classe Veicolo e si richiede di impostare il modello
                veicolo._Veicolo__set_modello(input("Indicare Modello: "))
            elif selezione == "3": # se si indica 3 allora si richiama il metodo privato della classe Veicolo e si richiede di impostare l'anno
                veicolo._Veicolo__set_anno(int(input("Indicare anno: ")))
            elif selezione == "4": # se si indica 4 allora si richiama il metodo privato della classe Veicolo e si stampa la marca
                print(veicolo._Veicolo__get_marca())
            elif selezione == "5": # se si indica 5 allora si richiama il metodo privato della classe Veicolo e si stampa il modello
                print(veicolo._Veicolo__get_modello())
            elif selezione == "6": # se si indica 6 allora si richiama il metodo privato della classe Veicolo e si stampa l'anno
                print(veicolo._Veicolo__get_anno())
            elif selezione == "7": # se si indica 7 allora si esce dal ciclo
                break
            else: # se si indica un valore diverso stampa un avviso
                print("Selezione non valida")