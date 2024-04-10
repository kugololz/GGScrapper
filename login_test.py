import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_exis_span(element):
    return element.name == 'span' and 'EXIS' in element.get_text()

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
        search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'codigo_fabricante')))
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.ENTER)
        item = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        stock_elements = soup.find_all('span', class_='mdl-card__stock')
        
        for stock_element in stock_elements:
            exis_span = soup.find(is_exis_span)

            if exis_span:       
                # Extract the text content of the span element
                stock_text = exis_span.get_text(strip=True)

                # Split the text to separate "EXIS" and the numeric value
                exis_text = ""
                numeric_value = ""
                for char in stock_text:
                    if char.isdigit():
                        numeric_value += char
                    else:
                        exis_text += char

                stock_amount = numeric_value.strip()
            
            if stock_amount != '0':
                print("Existen ", stock_amount, " en stock.")
            else:
                print("No hay productos en stock")

    

if __name__ == '__main__':
    # Inicialización del driver
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    lista = ['100-100000252BOX','BX8070811400', 'BX8070811700K']
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
