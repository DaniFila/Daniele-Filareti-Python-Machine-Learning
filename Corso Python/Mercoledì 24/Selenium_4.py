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

def dynamic_form(driver):
    """
    Visita https://demoqa.com/dynamic-properties
    Attendi che il bottone "Visible After 5 Seconds" appaia
    Cliccalo e verifica che l'azione sia stata eseguita con successo
    """
    # Il tuo codice qui
    driver.get("https://demoqa.com/dynamic-properties")
    time.sleep(6)
    pulsante = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/button[3]")
    pulsante.click()
    driver.quit()
    print("Pulsante apparso e cliccato!")


dynamic_form(driver)


