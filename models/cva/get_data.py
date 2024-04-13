import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def is_exis_span(element):
    return element.name == 'span' and 'EXIS' in element.get_text()

def decode(text):
    return text.encode(sys.stdout.encoding, errors = 'replace').decode(sys.stdout.encoding)

url = 'https://me2.grupocva.com/me/'

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

def select_category(driver, xpath_complete):
    category_select = driver.find_element(By.ID, 'send-search-filters')
    
    category_select = category_select.find_element(By.XPATH, xpath_complete)
    driver.execute_script("arguments[0].click();", category_select)
    # category_select.click()
    button_search = driver.find_element(By.ID, 'send-search-filters')
    button_search.click()

def scrape_cpu(driver):
    login(driver)
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[88]/input"
    driver.get(url)
    select_category(driver, xpath_complete) 
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    
    time.sleep(10)
    
    get_card_data = BeautifulSoup(driver.page_source, 'html.parser')
    info_elements = get_card_data.find_all('div', class_='demo-card-square mdl-card mdl-shadow--2dp col-md-3 no-padding')
    stock_elements = get_card_data.find_all('span', class_='mdl-card__stock')

    # print(stock_elements)

    with open('cpu_stock_info.txt', 'w') as f:
        for element in info_elements:
            f.write(str(element))

    with open('stock_info.txt', 'w') as f:
        for element in stock_elements:
            f.write(str(element))

    c = 1
    for element in stock_elements:
        exis_span = get_card_data.find(is_exis_span)
        print(exis_span)
        # if c%2 != 0:

        #     if exis_span:
        #         stock_text = exis_span.get_text(strip=True)
        #         print("Stock " + stock_text)
        #         exis_text = ""
        #         numeric_value = ""
        #         for char in stock_text:
        #             if char.isnumeric():
        #                 numeric_value += char
        #             else:
        #                 exis_text += char
        #         stock_amount = numeric_value.strip()
        #         print("Total " + stock_amount)
        #     # if stock_amount != 0:
        #     #     print("Existen ", stock_amount, " en stock.")
        #     # else: 
        #     #     print("No hay productos en el stock local")
        #     c += 1
        # else:
           # c += 1

if __name__ == '__main__':
    # Inicialización de la configuración del navegador
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    # Inicialización del driver
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox()
    # lista = ['100-100000252BOX','BX8070811400', 'BX8070811700K']
    # scrape(driver, lista)
    scrape_cpu(driver)

    # CPU array catcher
    # excel_file = '../../database.xlsx'
    # df = pd.read_excel(excel_file)

    # filtered_df = df[df['Categoria'].str.contains('CPU', case=False, na=False)]

    # cpu_skus = filtered_df['SKU']
    # cpu_skus_cleaned = cpu_skus.str.replace(r'\n', '', regex=True).str.replace('SKU: ', '')
    # cpu_list = []
    # for sku in cpu_skus_cleaned:
    #     cpu_list.append(sku)
        

    driver.quit()
