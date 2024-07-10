import requests
import json

def recupera_coordinate():
    città = input("Indicare nome città (in inglese): ")
    rec_coordinate = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={città}&count=1&language=it&format=json").text
    conversione_in_dizionario = json.loads(rec_coordinate)
    latitudine = conversione_in_dizionario["results"][0]['latitude']
    longitudine = conversione_in_dizionario["results"][0]['longitude']
    return latitudine,longitudine,città

def imposta_api(latitudine,longitudine):
    pioggia_b = False
    vento_b = False
    api = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m"
    dizionario = {"1":{"url":"&forecast_days=1","vento":True},"2":"&forecast_days=3","3":"","4":"&daily=wind_speed_10m_max","5":"&daily=precipitation_sum"}
    selezione_giorni = input("1: previsioni per un giorno\n2: previsioni per 3 giorni\n3: previsioni per 7 giorni\n")
    selezione_vento = input("vuoi anche le previsioni del vento? (4 per confermare): ")
    selezione_pioggia = input("vuoi anche le previsioni della pioggia? (5 per confermare): ")
    api+= dizionario[selezione_giorni]
    if selezione_vento == "4":
        api+=dizionario[selezione_vento]
        vento_b = True
    if selezione_pioggia == "5":
        api+=dizionario[selezione_pioggia]
        pioggia_b = True
    return api,pioggia_b,vento_b

def stampa_previsioni(api,città):
    meteo_g = requests.get(api).text
    meteo_dict = json.loads(meteo_g)
    print(f"\nLe previsioni per la città {città} sono:\n")
    orari = meteo_dict["hourly"]["time"]
    gradi = meteo_dict["hourly"]["temperature_2m"]
    for i in range(len(orari)):
        print(f"Orario: {orari[i]} Temperatura: {gradi[i]}\n")
    if pioggia_b:
        giorni_pioggia = meteo_dict["daily"]["time"]
        mm_pioggia = meteo_dict["daily"]["precipitation_sum"]
        for i in range(len(giorni_pioggia)):
            print(f"Giorno: {giorni_pioggia[i]} Millimetri della pioggia: {mm_pioggia[i]}")

latitudine,longitudine,città = recupera_coordinate()
     
api,pioggia_b,vento_b = imposta_api(latitudine,longitudine)

stampa_previsioni(api,città)