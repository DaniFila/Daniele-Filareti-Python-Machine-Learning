def lettura():
    with open("Giovedì 27/Es3.txt","r") as f:
        dati =f.read()
    return dati

def scrittura(d):
    with open("Giovedì 27/Es3.txt","w") as f:
        f.writelines(str(d))

def pulizia(a):
    inutili = ["[","]","{","}","\'"," "]
    for contenuto in inutili:
        a = a.replace(contenuto,"")
    a = a.replace(":",",")
    b = a.split(",")
    return b


def conversione(a):
    dizionario = {}
    for elemento in a:
        if elemento.isalpha():
            dizionario[elemento]= []
            nome = elemento
        else:
            dizionario[nome].append(int(elemento))
    return dizionario



database = lettura()
if database != "":    
    database = pulizia(database)
    database = conversione(database)
else:
    database = {}


print("\nGestione Database Studenti")
print("1. Visualizza elenco alunni e medie")
print("2. Aggiungi nuovo alunno")
print("3. Aggiungi voto a un alunno")
print("4. Elimina alunno")
print("5. Elimina voto di un alunno")
print("0. Esci")



while True:
    z = input("Inserire opzione: ")
    if z == "1":
        if database != "":
            for alunno in database:
                somma = 0
                count = 0
                for voti in database[alunno]:
                    somma+= voti
                    count+=1
                print("La media di", alunno, "è", somma/count)
        else:
            print("Il database è vuoto")
    elif z == "2":
        v = True
        nome = input("Inserire nome alunno: ")
        while not nome.isalpha:
            nome = input("Inserire nome alunno valido: ")
        database[nome] = []
        while v:
            v_materia = input("Inserire voto: ")
            while not v_materia.isnumeric:
                v_materia = input("Inserire voto materia valido: ")
            v_materia_i = int(v_materia)
            database[nome].append(v_materia_i)
            k = input("Vuoi continuare? (1/0): ")
            if k == "0":
                v = False
        scrittura(database)
    elif z == "3":
        if database != "":
            s_nome = input("Indicare il nome dell'alunno: ")
            if s_nome in database:
                s_voto = input("Indicare il voto: ")
                while not s_voto.isalnum():
                    s_voto = input("Indicare voto valido: ")
                database[s_nome].append(int(s_voto))
            else:
                print("Nome non presente in elenco")
            scrittura(database)
        else:
            print("Il database è vuoto")
    elif z == "4":
        if database != "":
            e_nome = input("Indicare nome alunno da eliminare: ")
            if e_nome in database:
                database.pop(e_nome)
                scrittura(database)
            else:
                print("Nome non presente")
        else:
            print("Il database è vuoto")  
    elif z == "5":
        if database != "":
            v_nome = input("Indicare nome alunno per voto da eliminare: ")
            if v_nome in database:
                print("I voti di",v_nome,"sono:",database[v_nome])
                while True:
                    voto = input("Indicare voto da eliminare: ")
                    while not voto.isalnum:
                        voto = input("Indicare voto valido da eliminare: ")
                    if int(voto) in database[v_nome]:
                        database[v_nome].remove(int(voto))
                        break
                    else:
                        print("Voto non presente tra i voti")
            else:
                print("Nome non presente in database")
        else:
            print("Il database è vuoto")
            
    elif z == "0":
        break
        







    






     
