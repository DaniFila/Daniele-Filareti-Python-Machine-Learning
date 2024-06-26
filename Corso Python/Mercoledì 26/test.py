dizionario_alunni = {"tommaso":[10,7,8]}

with open("file2.csv","r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")
diz_alu2 = {}
for element in righe:
    celle = element.split(",")
    diz_alu2[celle[0]] = []
    for voti in celle[1].split("-"):
        diz_alu2[celle[0]].append(voti)

print(diz_alu2)