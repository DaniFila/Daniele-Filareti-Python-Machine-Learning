from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

def advanced_scraping(driver):
    """
    Visita https://news.ycombinator.com/
    Estrai i titoli, i link e i punteggi dei primi 3 articoli
    Salva questi dati in un file CSV
    """
    # Il tuo codice qui
    driver.get("https://news.ycombinator.com/")
    #tit1 = driver.find_element(By.XPATH,"//*[@id=\"41057814\"]/td[3]/span/a")
    tit1 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/span/a")
    link1 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/span/span/a/span")
    tit2 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[4]/td[3]/span/a")
    link2 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[4]/td[3]/span/span/a/span")
    tit3 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[7]/td[3]/span/a")
    link3 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[7]/td[3]/span/span/a/span")
    punt1 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/span/span[1]")
    punt2 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/span/span[1]")
    punt3 = driver.find_element(By.XPATH,"/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[8]/td[2]/span/span[1]")
    titoli = [tit1.text,tit2.text,tit3.text]
    link = [link1.text,link2.text,link3.text]
    punteggi = [punt1.text,punt2.text,punt3.text]
    data = {"Titolo":titoli,"Link":link,"Punteggio":punteggi}
    df = pd.DataFrame(data)
    df.to_csv("Corso Python/Mercoledì 24/selenium_5.csv")
    print(df)

advanced_scraping(driver)
