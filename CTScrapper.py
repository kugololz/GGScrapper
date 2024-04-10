import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


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
        
        soup = BeautifulSoup(page_to_scrape, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = "ACTECK" if "acteck" in title.lower() else "VORAGO" if "vorago" in title.lower() else "EVOTEC" if "evotec" in title.lower() else "BALAM RUSH" if "balam rush" in title.lower() else "GAME FACTOR" if "game factor" in title.lower() else ""
                stock_string_cleaned = stock.strip().replace('\n', '').replace('[', '').replace(']', '')
                stock_number = stock_string_cleaned.split('\xa0')[0].strip()
                sku = sku.replace("(","")
                sku = sku.replace(")","")
                price_string = price
                price_string_cleaned = price_string.strip()
                price = price_string_cleaned[price_string_cleaned.index('$'):]
                price = price.replace(" MXN","")
                data.append(["PSU", sku, title, marca, "CT", stock_number, price])

        return data
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    
def scrape_GAB(driver, url):
    try:
        driver.get(url)
        page_to_scrape = driver.page_source
        
        soup = BeautifulSoup(page_to_scrape, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = "ACTECK" if "acteck" in title.lower() else "VORAGO" if "vorago" in title.lower() else "EVOTEC" if "evotec" in title.lower() else "BALAM RUSH" if "balam rush" in title.lower() else "GAME FACTOR" if "game factor" in title.lower() else "ASUS" if "asus" in title.lower() else "COOLER MASTER" if "cooler master" in title.lower() else "CORSAIR" if "corsair" in title.lower() else "DEEPCOOL" if "deepcool" in title.lower() else "GETTTECH" if "getttech" in title.lower() else "STYLOS" if "stylos" in title.lower() else "THERMALTAKE" if "thermaltake" in title.lower() else ""
                stock_string_cleaned = stock.strip().replace('\n', '').replace('[', '').replace(']', '')
                stock_number = stock_string_cleaned.split('\xa0')[0].strip()
                sku = sku.replace("(","")
                sku = sku.replace(")","")
                price_string = price
                price_string_cleaned = price_string.strip()
                price = price_string_cleaned[price_string_cleaned.index('$'):]
                price = price.replace(" MXN","")
                data.append(["Gabinete", sku, title, marca, "CT", stock_number, price])

        return data
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []    
    
def scrape_MB(driver, url):
    try:
        driver.get(url)
        page_to_scrape = driver.page_source
        
        soup = BeautifulSoup(page_to_scrape, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = ("ACER" if "acer" in title.lower() else
         "ACTECK" if "acteck" in title.lower() else
         "ADATA" if "adata" in title.lower() else
         "AMD" if "amd" in title.lower() else
         "AOC" if "aoc" in title.lower() else
         "APPLE" if "apple" in title.lower() else
         "ARUBA" if "aruba" in title.lower() else
         "ASUS" if "asus" in title.lower() else
         "AZOR" if "azor" in title.lower() else
         "ASUS BUSINESS" if "asus business" in title.lower() else
         "BENQ" if "benq" in title.lower() else
         "BIOSTAR" if "biostar" in title.lower() else
         "BROBOTIX" if "brobotix" in title.lower() else
         "BALAM RUSH" if "balam rush" in title.lower() else
         "BLACKPCS" if "blackpcs" in title.lower() else
         "COOLER MASTER" if "cooler master" in title.lower() else
         "CORSAIR" if "corsair" in title.lower() else
         "DELL" if "dell" in title.lower() else
         "DAHUA TECHNOLOGY" if "dahua technology" in title.lower() else
         "DEEPCOOL" if "deepcool" in title.lower() else
         "ECS" if "ecs" in title.lower() else
         "ELOTOUCH" if "elotouch" in title.lower() else
         "ENSON" if "enson" in title.lower() else
         "EVOTEC" if "evotec" in title.lower() else
         "EASY LINE" if "easy line" in title.lower() else
         "GAME FACTOR" if "game factor" in title.lower() else
         "GENERICO" if "generico" in title.lower() else
         "GETTTECH" if "getttech" in title.lower() else
         "GIGABYTE" if "gigabyte" in title.lower() else
         "GRANDSTREAM" if "grandstream" in title.lower() else
         "HIKVISION" if "hikvision" in title.lower() else
         "HP" if "hp" in title.lower() else
         "HYUNDAI" if "hyundai" in title.lower() else
         "HEWLETT PACKARD ENTERPRISE" if "hewlett packard enterprise" in title.lower() else
         "INTEL" if "intel" in title.lower() else
         "KENSINGTON" if "kensington" in title.lower() else
         "KINGSTON TECHNOLOGY" if "kingston technology" in title.lower() else
         "LANIX" if "lanix" in title.lower() else
         "LENOVO" if "lenovo" in title.lower() else
         "LG" if "lg" in title.lower() else
         "LOGITECH" if "logitech" in title.lower() else
         "MANHATTAN" if "manhattan" in title.lower() else
         "MICROSOFT" if "microsoft" in title.lower() else
         "MSI" if "msi" in title.lower() else
         "NECNON" if "necnon" in title.lower() else
         "NORTH SYSTEM" if "north system" in title.lower() else
         "NACEB TECHNOLOGY" if "naceb technology" in title.lower() else
         "NEXTEP" if "nextep" in title.lower() else
         "PERFECT CHOICE" if "perfect choice" in title.lower() else
         "PNY" if "pny" in title.lower() else
         "POLY" if "poly" in title.lower() else
         "PROVISION-ISR" if "provision-isr" in title.lower() else
         "QIAN" if "qian" in title.lower() else
         "REDRAGON" if "redragon" in title.lower() else
         "SAMSUNG" if "samsung" in title.lower() else
         "SANDISK" if "sandisk" in title.lower() else
         "SAXXON" if "saxxon" in title.lower() else
         "SEAGATE" if "seagate" in title.lower() else
         "STAR MICRONICS" if "star micronics" in title.lower() else
         "STARTECH.COM" if "startech.com" in title.lower() else
         "STYLOS" if "stylos" in title.lower() else
         "TARGUS" if "targus" in title.lower() else
         "TECHZONE" if "techzone" in title.lower() else
         "THERMALTAKE" if "thermaltake" in title.lower() else
         "TOSHIBA" if "toshiba" in title.lower() else
         "TRIPP-LITE" if "tripp-lite" in title.lower() else
         "VERBATIM" if "verbatim" in title.lower() else
         "VORAGO" if "vorago" in title.lower() else
         "WESTERN DIGITAL" if "western digital" in title.lower() else
         "XEROX" if "xerox" in title.lower() else
         "XPG" if "xpg" in title.lower() else
         "XZEAL" if "xzeal" in title.lower() else
         "YEYIAN" if "yeyian" in title.lower() else
         "ZEBRA" if "zebra" in title.lower() else "")

                stock_string_cleaned = stock.strip().replace('\n', '').replace('[', '').replace(']', '')
                stock_number = stock_string_cleaned.split('\xa0')[0].strip()
                sku = sku.replace("(","")
                sku = sku.replace(")","")
                price_string = price
                price_string_cleaned = price_string.strip()
                price = price_string_cleaned[price_string_cleaned.index('$'):]
                price = price.replace(" MXN","")
                data.append(["Motherboard", sku, title, marca, "CT", stock_number, price])

        return data
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []    
    
def scrape_GPU(driver, url):
    try:
        driver.get(url)
        page_to_scrape = driver.page_source
        
        soup = BeautifulSoup(page_to_scrape, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = ("ACER" if "acer" in title.lower() else
         "ACTECK" if "acteck" in title.lower() else
         "ADATA" if "adata" in title.lower() else
         "AMD" if "amd" in title.lower() else
         "AOC" if "aoc" in title.lower() else
         "APPLE" if "apple" in title.lower() else
         "ARUBA" if "aruba" in title.lower() else
         "ASUS" if "asus" in title.lower() else
         "AZOR" if "azor" in title.lower() else
         "ASUS BUSINESS" if "asus business" in title.lower() else
         "BENQ" if "benq" in title.lower() else
         "BIOSTAR" if "biostar" in title.lower() else
         "BROBOTIX" if "brobotix" in title.lower() else
         "BALAM RUSH" if "balam rush" in title.lower() else
         "BLACKPCS" if "blackpcs" in title.lower() else
         "COOLER MASTER" if "cooler master" in title.lower() else
         "CORSAIR" if "corsair" in title.lower() else
         "DELL" if "dell" in title.lower() else
         "DAHUA TECHNOLOGY" if "dahua technology" in title.lower() else
         "DEEPCOOL" if "deepcool" in title.lower() else
         "ECS" if "ecs" in title.lower() else
         "ELOTOUCH" if "elotouch" in title.lower() else
         "ENSON" if "enson" in title.lower() else
         "EVOTEC" if "evotec" in title.lower() else
         "EASY LINE" if "easy line" in title.lower() else
         "GAME FACTOR" if "game factor" in title.lower() else
         "GENERICO" if "generico" in title.lower() else
         "GETTTECH" if "getttech" in title.lower() else
         "GIGABYTE" if "gigabyte" in title.lower() else
         "GRANDSTREAM" if "grandstream" in title.lower() else
         "HIKVISION" if "hikvision" in title.lower() else
         "HP" if "hp" in title.lower() else
         "HYUNDAI" if "hyundai" in title.lower() else
         "HEWLETT PACKARD ENTERPRISE" if "hewlett packard enterprise" in title.lower() else
         "INTEL" if "intel" in title.lower() else
         "KENSINGTON" if "kensington" in title.lower() else
         "KINGSTON TECHNOLOGY" if "kingston technology" in title.lower() else
         "LANIX" if "lanix" in title.lower() else
         "LENOVO" if "lenovo" in title.lower() else
         "LG" if "lg" in title.lower() else
         "LOGITECH" if "logitech" in title.lower() else
         "MANHATTAN" if "manhattan" in title.lower() else
         "MICROSOFT" if "microsoft" in title.lower() else
         "MSI" if "msi" in title.lower() else
         "NECNON" if "necnon" in title.lower() else
         "NORTH SYSTEM" if "north system" in title.lower() else
         "NACEB TECHNOLOGY" if "naceb technology" in title.lower() else
         "NEXTEP" if "nextep" in title.lower() else
         "PERFECT CHOICE" if "perfect choice" in title.lower() else
         "PNY" if "pny" in title.lower() else
         "POLY" if "poly" in title.lower() else
         "PROVISION-ISR" if "provision-isr" in title.lower() else
         "QIAN" if "qian" in title.lower() else
         "REDRAGON" if "redragon" in title.lower() else
         "SAMSUNG" if "samsung" in title.lower() else
         "SANDISK" if "sandisk" in title.lower() else
         "SAXXON" if "saxxon" in title.lower() else
         "SEAGATE" if "seagate" in title.lower() else
         "STAR MICRONICS" if "star micronics" in title.lower() else
         "STARTECH.COM" if "startech.com" in title.lower() else
         "STYLOS" if "stylos" in title.lower() else
         "TARGUS" if "targus" in title.lower() else
         "TECHZONE" if "techzone" in title.lower() else
         "THERMALTAKE" if "thermaltake" in title.lower() else
         "TOSHIBA" if "toshiba" in title.lower() else
         "TRIPP-LITE" if "tripp-lite" in title.lower() else
         "VERBATIM" if "verbatim" in title.lower() else
         "VORAGO" if "vorago" in title.lower() else
         "WESTERN DIGITAL" if "western digital" in title.lower() else
         "XEROX" if "xerox" in title.lower() else
         "XPG" if "xpg" in title.lower() else
         "XZEAL" if "xzeal" in title.lower() else
         "YEYIAN" if "yeyian" in title.lower() else
         "ZEBRA" if "zebra" in title.lower() else "")

                stock_string_cleaned = stock.strip().replace('\n', '').replace('[', '').replace(']', '')
                stock_number = stock_string_cleaned.split('\xa0')[0].strip()
                sku = sku.replace("(","")
                sku = sku.replace(")","")
                price_string = price
                price_string_cleaned = price_string.strip()
                price = price_string_cleaned[price_string_cleaned.index('$'):]
                price = price.replace(" MXN","")
                data.append(["GPU", sku, title, marca, "CT", stock_number, price])

        return data
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []    

def scrape_CPU(driver, url):
    try:
        driver.get(url)
        page_to_scrape = driver.page_source
        
        soup = BeautifulSoup(page_to_scrape, 'html.parser')
        items_div = soup.find('div', class_="ct-result-list")
        if items_div:
            titulos = [safe_decode(title.text) for title in items_div.findAll("h5")]
            skus = [sku.text for sku in items_div.findAll('h7')]
            prices = [price.text for price in items_div.findAll('div', class_='ct-current')]
            stocks = [stock.text for stock in items_div.findAll('div', class_='ct-availability')]
        data = []
        for sku, title, price, stock in zip(skus, titulos, prices, stocks):
                marca = "AMD" if "amd" in title.lower() else "INTEL" if "intel" in title.lower() else ""
                stock_string_cleaned = stock.strip().replace('\n', '').replace('[', '').replace(']', '')
                stock_number = stock_string_cleaned.split('\xa0')[0].strip()
                sku = sku.replace("(","")
                sku = sku.replace(")","")
                price_string = price
                price_string_cleaned = price_string.strip()
                price = price_string_cleaned[price_string_cleaned.index('$'):]
                price = price.replace(" MXN","")
                data.append(["CPU", sku, title, marca, "CT", stock_number, price])

        return data
    
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    
    
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)
    data_PSU = scrape_PSU(driver, 'https://ctonline.mx/Ensamble/Fuentes-de-Poder/?categoriaM=COMPONENTES&s[0]=17&')
    data_GAB = scrape_GAB(driver, 'https://ctonline.mx/Ensamble/Gabinetes-para-Computadoras/?&categoriaM=COMPONENTES&s[0]=17&')
    data_MB = scrape_MB(driver, 'https://ctonline.mx/Marca/450/?categoria[109]=Motherboards&categoriaM=COMPONENTES&s[0]=17&')
    data_GPU = scrape_GPU(driver, 'https://ctonline.mx/Marca/450/?categoria[156]=Tarjetas%20de%20Video&categoriaM=COMPONENTES&s[0]=17&')
    data_CPU = scrape_CPU(driver, 'https://ctonline.mx/Ensamble/Microprocesadores/?marca=0&s[0]=17')
    
    df_PSU = pd.DataFrame(data_PSU, columns=["CATEGORIA", "SKU", "DESCRIPCION", "MARCA", "PROVEEDOR", "STOCK", "PRECIO"])
    df_GAB = pd.DataFrame(data_GAB, columns=["CATEGORIA", "SKU", "DESCRIPCION", "MARCA", "PROVEEDOR", "STOCK", "PRECIO"])
    df_MB = pd.DataFrame(data_MB, columns=["CATEGORIA", "SKU", "DESCRIPCION", "MARCA", "PROVEEDOR", "STOCK", "PRECIO"])
    df_GPU = pd.DataFrame(data_GPU, columns=["CATEGORIA", "SKU", "DESCRIPCION", "MARCA", "PROVEEDOR", "STOCK", "PRECIO"])
    df_CPU = pd.DataFrame(data_CPU, columns=["CATEGORIA", "SKU", "DESCRIPCION", "MARCA", "PROVEEDOR", "STOCK", "PRECIO"])
    
    frames = [df_PSU, df_GAB, df_MB, df_GPU, df_CPU]
    result = pd.concat(frames)

    
    driver.quit()
    result.to_excel("CT.xlsx", index=False)
