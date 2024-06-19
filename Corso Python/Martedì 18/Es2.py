# aggiungi = 1
# rimuovi = 2     
# sostituisci = 3

a="ciao pippo baudo"                   # variabile contenente stringhe 

print("selezionare azione ")
print("")
print("aggiungi 1 ")                   # varie stampe per indirizzare l'utente
print("rimuovi 2 ")
print("sostituisci 3 ")


b=int(input("indicare azione "))    # variabile per indicare azione da svolgere presa da input

if b==1:
    a = a + " " + input("inserire parola ")      # operazione di aggiunta di stringa presa in input
elif b==2:
    z = input("indicare stringa da eliminare ")     # selezione di stringa da eliminare (indicare stringa contenuta in a)
    a = a.replace(z, "")
elif b==3:
    c = input("inserisci la stringa da sostituire ")     # in input si richiede stringa da sostituire già presente
    a = a.replace(c,input("nuova stringa "))         # nuova stringa presa in input sostitutiva


print(a)        # stampa della variabile a contenente la stringa manipolata