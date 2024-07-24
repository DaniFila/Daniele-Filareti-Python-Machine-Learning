from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def setup_driver():
    """
    Configura e restituisce un'istanza del WebDriver di Chrome.
    """
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Esecuzione in background
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    return driver
driver = setup_driver()

def table_scraping(driver):
    """
    Visita https://www.w3schools.com/html/html_tables.asp
    Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile
    """
    # Il tuo codice qui
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    termini = driver.find_element(By.ID,"accept-choices")
    termini.click()
    tabella = driver.find_element(By.ID,"customers")
    contenuto = tabella.text
    return contenuto

def contenuto_leggibile(contenuto):
    tabella = []
    righe = contenuto.split("\n")
    for riga in righe[1:]:
        elementi = riga.split(" ")
        tabella.append([" ".join(elementi[0:-3])," ".join(elementi[-3:-1]),elementi[-1]])
    colonne = righe[0].split()
    df = pd.DataFrame(tabella,columns=colonne)
    print(df)




contenuto = table_scraping(driver)

contenuto_leggibile(contenuto)