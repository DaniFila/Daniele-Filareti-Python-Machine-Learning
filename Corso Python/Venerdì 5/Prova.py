# EREDITARIETA'

class Padre: # questa è la classe padre con al costruttore nome e cognome e un metodo che stampa informazioni
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    
    def info(self):
        print(f"Ciao, il mio nome è {self.nome} e il mio cognome è {self.cognome}!")


class Figlia(Padre): # questa è la classe figlia che eredita dalla classe Padre gli attributi e i metodi
    def __init__(self, nome, cognome):
        Padre.__init__(self,nome, cognome)
    


papà = Padre("Pippo","Baudo") # creo oggetto Padre
figlio = Figlia("Stella","Russo") # creo oggetto Figlia


papà.info() # richiamo metodo info 
figlio.info() # richiamo metodo info della classe Padre
    
# L'ereditarietà ci permette quindi in una classe di ereditare attributi e metodi di una classe padre, inoltre in python,
# possiamo in una classe ereditare da più classi, è possibile usare la funzione super() per richiamare metodi della classe padre
# e possiamo sovrascrivere metodi della classe padre per riutilizzarla nel contesto della classe figlia con qualche cambiamento.
#---------------------------------------------------------------------------------------------------------------------------------------






# PROPRIETARIETA'

class Login: # creo classe login
    def __init__(self,username): # nel costruttore avrò attributo username pubblico e attributo password privato, si passa solo l'username al momento della creazione
        self.username = username
        self.__password = ""
    
    def set_password(self,psw): # metodo set per impostare password che si passa al richiamo del metodo
        self.__password = psw

    def __get_password(self): # metodo get privato per ricevere la password
        return self.__password
    


user = Login("Pippo1122") # creo oggetto di tipo Login passando l'username

user.set_password("ciao123") # per impostare la password richiamo metodo set

# essendo privato il metodo get non è possibile richiamarlo normalmente come un'altro metodo, possiamo per esempio utilizzarlo creando una ipotetica classe con permessi maggiori in un contesto di login
# per poterla avere e visualizzarla

# per visualizzarla si può fare così:
print(user._Login__get_password()) # è ovviamente sconsigliato questo utilizzo fuori dai contesti delle classi

# La proprietarietà ci permette di nascondere e rendere privati attributi e metodi delle classi, esistono anche metodi e attributi protetti che sono contrassegnati con un _ davanti il nome, mentre quello privato con il doppio __
# i metodi e attributi protetti sono da indicazione per i programmatori senza avere un cambiamento funzionale rispetto quelli pubblici
#---------------------------------------------------------------------------------------------------------------------------------------


# POLIMORFISMO

class Veicolo:  # classe padre
    def muovi(self):  # metodo muovi 
        pass


class Automobile(Veicolo): # classe figlia
    def muovi(self): # riutilizza il metodo del padre sovrascrivendolo
        print("L'automobile è in movimento")

class Barca(Veicolo): # classe figlia
    def muovi(self): # riutilizza il metodo del padre sovrascrivendolo
        print("La barca si muove in acqua.")


auto = Automobile() # creazione oggetti
barca = Barca()

auto.muovi() # test
barca.muovi()


# Il polimorfismo è quel principio che ci permette di riutilizzare del codice, il riutilizzo del codice può avvenire come in questo esempio semplice
# che dalla classe padre si sovrascrive il metodo muovi, facendola cambiare forma ma non il suo comportamento.