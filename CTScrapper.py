import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def safe_decode(text):
    return text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)


def login(driver):

    driver.get('https://ctonline.mx/iniciar/correo')
    
    login_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'form')))
    #Rellenamos el formulario de inicio de sesion
    username_field = login_form.find_element(By.NAME,'correo')
    password_field = login_form.find_element(By.NAME,'password')

    username_field.send_keys('administracion@grupordc.com.mx')
    password_field.send_keys('JuanPablo#1645')

    submit_button = login_form.find_element(By.CLASS_NAME,'btn-light-blue')
    submit_button.click()
    print('Logeo exitoso en plataforma CT.')
    
def scrape_PSU(driver, url):
    try:
        driver.get(url)
        page_to_scrape = driver.page_source
        
        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = "ACTECK" if "acteck" in title.lower() else "VORAGO" if "vorago" in title.lower() else "EVOTEC" if "evotec" in title.lower() else "BALAM RUSH" if "balam rush" in title.lower() else "GAME FACTOR" if "game factor" in title.lower() else ""
                data.append(["PSU", sku, title, marca, "CT", stock, price])
        print (data)
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)
    scrape_PSU(driver, 'https://ctonline.mx/Ensamble/Fuentes-de-Poder/?categoriaM=COMPONENTES&s[0]=17&')
    driver.quit()
    