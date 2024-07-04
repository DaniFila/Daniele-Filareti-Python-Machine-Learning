import modV


gestione_veicoli = modV.GestoreParcoVeicoli()
veicolo1 = modV.Veicolo()

# gestione_veicoli.gestore(veicolo1)

veicolo2 = modV.Veicolo()
veicolo3 = modV.Veicolo()

# gestione_veicoli.aggiungi_veicolo(veicolo2)

# gestione_veicoli.aggiungi_veicolo(veicolo3)

# gestione_veicoli.rimuovi_veicolo("Lamborghini","Urus")
gestione_veicoli.rimuovi_veicolo("ferrari","roma")
gestione_veicoli.lista_veicoli()