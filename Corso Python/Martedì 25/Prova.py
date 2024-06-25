alunni={}
while True:
    v = True
    nome = input("Inserire nome alunno: ")
    while not nome.isalpha:
        nome = input("Inserire nome alunno valido: ")
    alunni[nome] = {}
    while v:
        v_materia = input("Inserire voto materia: ")
        while not v_materia.isnumeric:
            v_materia = input("Inserire voto materia valido: ")
        v_materia_f = float(v_materia)
        alunni[nome] = v_materia_f

        k = input("Vuoi continuare? (1/0): ")
        if k == "0":
            v = False
    j = input("Vuoi aggiungere alunno? (1/0): ")
    if j == "0":
        break


print(alunni)

