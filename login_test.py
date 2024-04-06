import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def decode(text):
    return text.encode(sys.stdout.encoding, errors = 'replace').decode(sys.stdout.encoding)

def login(driver):
    
    driver.get('https://me2.grupocva.com/me/inicio.php#')

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'top-login-nav-trigger')))
    login_button.click()

    login_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'frm')))

    #Completar el formulario de inicio de sesion
    username_field = login_form.find_element(By.ID, 'fUsuario')
    password_field = login_form.find_element(By.ID, 'fContrasenia')

    # Credenciales de inicio de sesion
    username_field.send_keys('admin73688')
    password_field.send_keys('Juanpablo1645')

    submit_button = login_form.find_element(By.ID, 'entrar')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be('https://me2.grupocva.com/me/'))
    print('Login successful')

def scrape(driver, lista_de_busqueda):
    
    login(driver)
    
    for search_query in lista_de_busqueda:
        search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'busqueda_libre')))
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 100)
        wait
    
    

if __name__ == '__main__':
    # Inicialización del driver
    driver = webdriver.Chrome()
    lista = [1,2,3]
    scrape(driver, lista)

    # CPU array catcher
    excel_file = 'database.xlsx'
    df = pd.read_excel(excel_file)

    filtered_df = df[df['Categoria'].str.contains('CPU', case=False, na=False)]

    cpu_skus = filtered_df['SKU']
    cpu_skus_cleaned = cpu_skus.str.replace(r'\n', '', regex=True).str.replace('SKU: ', '')
    cpu_list = []
    for sku in cpu_skus_cleaned:
        cpu_list.append(sku)
        
        

    driver.quit()
