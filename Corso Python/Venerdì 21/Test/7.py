# DOMANDA 7
vocali = "aeiouAEIOU"    # stringa contenente vocali sia maiuscole che minuscole
stringa = input("Inserire una stringa: ")   # stringa da input
count = 0  # contatore per vocali
for i in range(len(stringa)):   # scan dei caratteri della stringa attraverso la len della stringa
    if stringa[i] in vocali:   # se il carattere si trova nella stringa vocali il contatore si incrementa
        count+=1



print("La stringa", stringa, "contiene", count, "vocali")   # stampa finale