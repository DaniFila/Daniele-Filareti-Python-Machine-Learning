if corso.find("corso").text == corso_S:
                        print("Corso trovato!")
                        select = input("1: modifica nome\n2: modifica voto\n")
                        if select == "1":
                            corso.find("nome").text = input("Inserisci nuovo nome: ")
                        elif select == "2":
                            corso.find("voto").text = input("Inserire voto modificato: ")
                        else:
                            print("Scelta non valida.")