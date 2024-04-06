from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
#change
def safe_decode(text):
    return text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

def scrape_page_CPU(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "AMD" if "AMD" in title else "INTEL" if "Intel" in title else ""
            data.append(["CPU", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    
def scrape_page_MB(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "AMD" if "AMD" in title else "AORUS" if "AORUS" in title else "ASROCK" if "ASRock" in title else "ASUS" if "ASUS" in title else "BIOSTAR" if "Biostar" in title else "ECS" if "ECS" in title else "GIGABYTE" if "Gigabyte" in title else "MSI" if "MSI" in title else "NZXT" if "NZXT" in title else ""
            data.append(["Motherboard", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

def scrape_page_GPU(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "AMD" if "AMD" in title else "AORUS" if "AORUS" in title else "ASROCK" if "ASRock" in title else "ASUS" if "ASUS" in title else "EVGA" if "EVGA" in title else "GIGABYTE" if "Gigabyte" in title else "LENOVO" if "Lenovo" in title else "MSI" if "MSI" in title else "PALIT" if "Palit" in title else "PNY" if "PNY" in title else "POWERCOLOR" if "PowerColor" in title else "SAPPHIRE" if "Sapphire" in title else "XFX" if "XFX" in title else "ZOTAC" if "Zotac" in title else ""
            data.append(["GPU", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    
def scrape_page_GAB(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "ACTECK" if "Acteck" in title else "AEROCOOL" if "AeroCool" in title else "ASUS" if "ASUS" in title else "BALAMRUSH" if "Balam Rush" in title else "COOLER MASTER" if "Cooler Master" in title else "CORSAIR" if "Corsair" in title else "COUGAR" if "Cougar" in title else "DEEPCOOL" if "DeepCool" in title else "FRACTAL DESIGN" if "Fractal Design" in title else "IN WIN" if "In Win" in title else "MUNFROST" if "Munfrost" in title else "NZXT" if "NZXT" in title else "THERMALTAKE" if "Thermaltake" in title  else "XPG" if "XPG" in title else "YEYIAN" if "Yeyian" in title else ""
            data.append(["Gabinete", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

def scrape_page_PSU(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "ACTECK" if "acteck" in title.lower() else "AEROCOOL" if "aerocool" in title.lower() else "ASUS" if "asus" in title.lower() else "BALAMRUSH" if "balam rush" in title.lower() else "COOLER MASTER" if "cooler master" in title.lower() else "CORSAIR" if "corsair" in title.lower() else "EVGA" if "evga" in title.lower() else "GIGABYTE" if "gigabyte" in title.lower() else "IN WIN" if "in win" in title.lower() else "MSI" if "MSI" in title else "NZXT" if "NZXT" in title else "SEASONIC" if "seasonic" in title.lower() else "THERMALTAKE" if "thermaltake" in title.lower() else "XPG" if "xpg" in title.lower() else "YEYIAN" if "yeyian" in title.lower() else ""
            data.append(["PSU", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

def scrape_page_EL(url):
    try:
        page_to_scrape = requests.get(url)
        page_to_scrape.raise_for_status()  

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        
        skus = [sku.text for sku in soup.findAll("div", class_="emproduct_right_artnum")]

        prices = [price.text for price in soup.findAll("label", class_="price")]

        titles = [safe_decode(title.text) for title in soup.findAll("a", id=lambda x: x and x.startswith("productList-"))]

        stock = [div.find("span").text.strip() for div in soup.findAll("div", class_="emstock")]

        data = []
        for sku, title, price, stock_status in zip(skus, titles, prices, stock):
            marca = "AEROCOOL" if "aerocool" in title.lower() else "AORUS" if "aorus" in title.lower() else "ASUS" if "asus" in title.lower() else "BALAM RUSH" if "balam rush" in title.lower() else "COOLER MASTER" if "cooler master" in title.lower() else "CORSAIR" if "corsair" in title.lower() else "COUGAR" if "cougar" in title.lower() else "DEEPCOOL" if "deepcool" in title.lower() else "EVGA" if "evga" in title.lower() else "GAMDIAS" if "gamdias" in title.lower() else "GAME FACTOR" if "game factor" in title.lower() else "IN WIN" if "in win" in title.lower() else "LIAN LI" if "lian li" in title.lower() else "MSI" if "MSI" in title else "NACEB TECHNOLOGY" if "naceb technology" in title.lower() else "NZXT" if "nzxt" in title.lower() else "OCELOT GAMING" if "ocelot gaming" in title.lower() else "TEAM GROUP" if "team group" in title.lower() else "THERMALTAKE" if "thermaltake" in title.lower() else "XPG" if "xpg" in title.lower() else "XZEAL" if "xzeal" in title.lower() else "YEYIAN" if "yeyian" in title.lower() else ""
            data.append(["Enfriamiento Liquido", sku, title, marca, "Cyberpuerta", stock_status, price])

        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
    


cpu_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/"
mb_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-Madre/"
gpu_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-de-Video/"
gabinete_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Gabinetes/"
psu_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Fuentes-de-Poder-para-PC-s/"
enfriamiento_url = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Enfriamiento-y-Ventilacion/Enfriamiento-Liquido/"


all_data = []  
print("Actualizando la base de datos por favor espere . . .")
# Loop contenido en los CPUs
page_number = 1  
while True:
    url1 = cpu_url if page_number == 1 else f"{cpu_url}{page_number}/"
    
    data = scrape_page_CPU(url1)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1 


# Loop contenido en las Tarjetas Madre
page_number = 1 
while True:
    url2 = mb_url if page_number == 1 else f"{mb_url}{page_number}/"
    
    data = scrape_page_MB(url2)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1

# Loop contenido en las GPUs
page_number = 1 
while True:
    url3 = gpu_url if page_number == 1 else f"{gpu_url}{page_number}/"
    
    data = scrape_page_GPU(url3)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1

# Loop contenido en los gabinetes
page_number = 1 
while True:
    url4 = gabinete_url if page_number == 1 else f"{gabinete_url}{page_number}/"
    
    data = scrape_page_GAB(url4)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1

# Loop contenido en las PSUs
page_number = 1 
while True:
    url5 = psu_url if page_number == 1 else f"{psu_url}{page_number}/"
    
    data = scrape_page_PSU(url5)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1
    
# Loop contenido en los enfriamientos
page_number = 1 
while True:
    url3 = enfriamiento_url if page_number == 1 else f"{enfriamiento_url}{page_number}/"
    
    data = scrape_page_EL(url3)
    
    if not data:
        break  
    
    all_data.extend(data)  
    page_number += 1   
    
#Creacion del Excel
df = pd.DataFrame(all_data, columns=['Categoria','SKU','Titulo','Marca','Proveedor','Stock','Costo'])

df.to_excel('database.xlsx', index=False)
print("Se ha concluido la operacion con exito!")

