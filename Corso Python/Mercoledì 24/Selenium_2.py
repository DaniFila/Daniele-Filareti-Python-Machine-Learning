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


def practice_login(driver):
    """
    Visita https://practicetestautomation.com/practice-test-login/
    Effettua il login con username "student" e password "Password123"
    Verifica che il login sia avvenuto con successo
    """
    
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.NAME,"username")
    password = driver.find_element(By.NAME,"password")
    username.send_keys("student")
    password.send_keys("Password123")
    submit = driver.find_element(By.ID,"submit")
    submit.click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"post-title")))
    result = driver.find_element(By.CLASS_NAME,"post-title")
    print(result.text)


driver = setup_driver()
practice_login(driver)

