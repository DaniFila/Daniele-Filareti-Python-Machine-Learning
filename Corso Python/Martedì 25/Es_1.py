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
    j = input("Vuoi aggiungere alunno? (1/0): ")
    if j == "0":
        break



for alunno in alunni:
    somma = 0
    count = 0
    for materia in alunni[alunno]:
        somma+= alunni[alunno][materia]
        count+=1
    print("La media di", alunno, "è", somma/count)  
     
