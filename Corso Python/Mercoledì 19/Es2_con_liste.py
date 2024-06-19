

L=[]                    

print("selezionare azione ")
print("")
print("aggiungi 1 ")                   
print("rimuovi 2 ")
print("sostituisci 3 ")
print("visualizza 4 ")
print("riordina 5")
print("esci 6 ")

while True:
    b=int(input("indicare azione ")) 
    if b==1:
        L.append(input("Inserire Stringa nuova "))
    elif b==2:
        c = input("indicare stringa da rimuovere ")
        if c in L:
            L.remove(c)
        else:
            print("elemento non presente")
    elif b==3:
        d = input("indicare elemento da sostituire ")
        if d in L:
            L.remove(d)
            L.append(input("inserire elemento da inserire "))
        else:
            print("elemento non presente")
    elif b==6:
        break
    elif b==4:
        for i in range(len(L)):
            print(L[i])
    elif b==5:
        L.sort()    
    else:
        print("operazione non valida")





             
