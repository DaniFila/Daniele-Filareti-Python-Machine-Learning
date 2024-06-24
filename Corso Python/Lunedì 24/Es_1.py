a = input("Inserire il tuo nome: ")
b = int(input("Inserire il tuo anno di nascita: "))
c = int(input("Inserire giorno della settimana: "))
età = 0
for i in range(b,2024):
    età+=1

weekend = 0
for i in range(c,6):
    weekend+=1
print("Il tuo nome è", a,"hai",età,"e mancano",weekend,"al weekend")

