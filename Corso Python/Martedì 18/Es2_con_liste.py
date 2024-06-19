# aggiungi = 1
# rimuovi = 2     
# sostituisci = 3

L=[]                    

print("selezionare azione ")
print("")
print("aggiungi 1 ")                   # varie stampe per indirizzare l'utente
print("rimuovi 2 ")
print("sostituisci 3 ")
print("esci 4 ")

while True:
    b=int(input("indicare azione ")) 
    if b==1:
        L.append(input("Inserire Stringa nuova"))
    elif b==2:
        c = input("indicare stringa da rimuovere")
        if c in L:
            L.remove(c)
        else:
            print("elemento non presente")
    elif b==3:
        d = print("indicare elemento da sostituire")
        if d in L:
            L.remove(d)
            L.append(input(""))
        else:
            print("elemento non presente")
    elif b==4:
        break
    else:
        print("operazione non valida")


print(L)                                    


             
