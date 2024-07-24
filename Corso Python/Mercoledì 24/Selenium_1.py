from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    """
    Configura e restituisce un'istanza del WebDriver di Chrome.
    """
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Esecuzione in background
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    return driver


def wikipedia_search(driver):
    driver.get("https://it.wikipedia.org/wiki/Pagina_principale")
    barra_ricerca = driver.find_element(By.NAME,"search")
    barra_ricerca.clear()
    barra_ricerca.send_keys("Python (programming language)" + Keys.RETURN)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"results-info")))

    primo_paragrafo = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li[1]/div/div[2]/div[2]")
    print(primo_paragrafo.text)


driver = setup_driver()

wikipedia_search(driver)