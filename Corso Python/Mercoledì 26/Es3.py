def lettura():
    with open("Mercoledì 26/Es3.csv","r") as f:
        dati =f.read()
    return dati

def scrittura(d):
    with open("Mercoledì 26/Es3.csv","w") as f:
        f.writelines(d)


alunni={}

while True:
    v = True
    nome = input("Inserire nome alunno: ")
    while not nome.isalpha:
        nome = input("Inserire nome alunno valido: ")
    alunni[nome] = {}
    while v:
        materia = input("Inserire la materia: ")
        alunni[nome][materia] = {}
        v_materia = input("Inserire voto materia: ")
        while not v_materia.isnumeric:
            v_materia = input("Inserire voto materia valido: ")
        v_materia_f = float(v_materia)
        alunni[nome][materia] = v_materia_f
        k = input("Vuoi continuare? (1/0): ")
        if k == "0":
            v = False
    break

t = "dani,7,8.5,9\npippo,9,9,5,6,8,7"

r = t.split("\n")

print(r)
dict1={}
for element in r:
    valori = element.split(",")
    print(valori)
    



"""printMenù
        Stampa media e voti: 1
        aggiungi studente e voto: 2
        elimina studente: 3
        elimina voto: 4
        aggiungi voto: 5 
z = input("Indicare scelta: ")



for alunno in alunni:
    somma = 0
    count = 0
    for materia in alunni[alunno]:
        somma+= alunni[alunno][materia]
        count+=1
    print("La media di", alunno, "è", somma/count)"""
     
