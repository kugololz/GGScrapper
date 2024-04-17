import re
import time
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def decode(text):
    return text.encode(sys.stdout.encoding, errors = 'replace').decode(sys.stdout.encoding)

urls = {
    "home": 'https://me2.grupocva.com/me/',
    "to_scrape": 'https://me2.grupocva.com/me/pedidos/index.php?page='
}

xpaths = {

}

url = 'https://me2.grupocva.com/me/'
url_scraped = 'https://me2.grupocva.com/me/pedidos/index.php?page='
brands = [
    "ASROCK", "MSI", "GIGABYTE" "INTEL", "PNY", "XFX", "ASUS", "BIOSTAR",
    "ECS", "NZXT", "ACTECK", "XPG", "BALAM RUSH", "COOLER MASTER", "CORSAIR",
    "OCELOT"
]

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

def select_category(driver, xpath_complete, subcategory = ""):
    category_select = driver.find_element(By.ID, 'send-search-filters')
    
    select_local = category_select.find_element(By.XPATH, "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[1]/div/div/label[1]/input")
    driver.execute_script("arguments[0].click();", select_local)
    category_select = category_select.find_element(By.XPATH, xpath_complete)
    driver.execute_script("arguments[0].click();", category_select)
    if subcategory != "":
        time.sleep(6)
        category_select = driver.find_element(By.CLASS_NAME, 'view-subgpos')
        subcategory_select = category_select.find_element(By.XPATH, subcategory)
        driver.execute_script("arguments[0].click();", subcategory_select)

    # category_select.click()
    button_search = driver.find_element(By.ID, 'send-search-filters')
    button_search.click()

scrape_card_elements = '''
card_content = document.querySelectorAll('.demo-card-square.mdl-card.mdl-shadow--2dp.col-md-3.no-padding');
console.log(card_content);
list_object = [];
    card_content.forEach(div_content => {
        console.log(div_content);
        span = div_content.querySelector('span.mdl-card__stock');
        spanExist = span.textContent.trim().replace(/\s+/g, '');
        matches = spanExist.match(/EXIS(\d+)/);
        console.log(matches)
        product_object = { category:'', code: '', cp: '', description: '', brand: '', obtained_from: 'cva', existence: 0, price: 0 };
        console.log(product_object);
        if (matches) {
            if (parseInt(matches[1]) > 0) {
                text_complete = div_content.querySelectorAll('.mdl-card__supporting-text.is-height-desc.d-inline-flex.justify-content-md-center.align-items-center');
                cp = div_content.querySelector('.mdl-card__title-text');
                price_complete = div_content.querySelector('.mdl-card__legend-promo-price.d-inline-flex.justify-content-md-center.align-items-center')
                price = (price_complete) ? price_complete.innerText.split(`\n`)[1].split(' ')[0]: 0.0;
                comp = (text_complete) ? text_complete[0].innerText: '';
                parts = comp.split(`\n`);
                product_object.code = parts[0].split(':')[1].trim();
                product_object.description = (parts.length > 2) ? parts[2].trim():parts[1].trim();
                product_object.cp = cp.textContent.trim();
                product_object.price = parseFloat(price);
                product_object.existence = parseInt(matches[1]);
                console.log(product_object);
                list_object.push(product_object);
            }
        }
    });
console.log(list_object);
return list_object
'''

def scrape_cpu(driver, url_scrape):
    try:
        driver.get(url_scrape)
        time.sleep(3)
        list_object = driver.execute_script(scrape_card_elements)
        data = list_object
        for product in data:
            product["category"] = "CPU"
            product["brand"] = 'INTEL' if re.search(r'\b(INTEL)\b', product["description"], re.I) else 'AMD'
        return data
    except TimeoutException:
        print("Tiempo de espera excedido.")
        
    except NoSuchElementException:
        print("Elemento no encontrado.")
        
    except Exception as e:
        print("Ocurrió un error:", e)

def scrape_gpu(driver, url_scrape):
    driver.get(url_scrape)
    time.sleep(5)
    list_object = driver.execute_script(scrape_card_elements)
    data = list_object

    for product in data:
        product["category"] = "GPU"
        for brand in brands:
            if re.search(r'\b' + brand + r'\b', product["description"], re.I):
                product["brand"] = brand
                break
    
    return data

def scrape_mb(driver, url_scrape):
    driver.get(url_scrape)
    time.sleep(5)
    list_object = driver.execute_script(scrape_card_elements)
    data = list_object

    for product in data:
        product["category"] = "Motherboard"
        for brand in brands:
            if re.search(r'\b' + brand + r'\b', product["description"], re.I):
                product["brand"] = brand
                break

    return data

def scrape_gab(driver, url_scrape):
    driver.get(url_scrape)
    time.sleep(5)
    list_object = driver.execute_script(scrape_card_elements)
    data = list_object

    for product in data:
        product["category"] = "Gabinete"
        for brand in brands:
            if re.search(r'\b' + brand + r'\b', product["description"], re.I):
                product["brand"] = brand
                break
    
    return data

def scrape_psu(driver, url_scrape):
    driver.get(url_scrape)
    time.sleep(5)
    list_object = driver.execute_script(scrape_card_elements)
    data = list_object

    for product in data:
        product["category"] = "PSU"
        for brand in brands:
            if re.search(r'\b' + brand + r'\b', product["description"], re.I):
                product["brand"] = brand
                break

    return data

def scrape_cooler(driver, url_scrape):
    try: 
        driver.get(url_scrape)
        time.sleep(5)
        list_object = driver.execute_script(scrape_card_elements)
        data = list_object

        for product in data:
            if re.search(r'\bENFRIAMIENTO LIQUIDO\b', product["description"], re.IGNORECASE):
                product["category"] = "Enfriamiento Liquido"
                for brand in brands:
                    if re.search(r'\b' + brand + r'\b', product["description"], re.I):
                        product["brand"] = brand
                        break

        return data
    except TimeoutException:
        print("Tiempo de espera excedido.")
        return []
        
    except NoSuchElementException:
        print("Elemento no encontrado.")
        return []

if __name__ == '__main__':
    # Inicialización de la configuración del navegador
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    # Inicialización del driver
    driver = webdriver.Chrome(options=options)

    all_components = []

    # Inicion de sesion
    login(driver)
    # driver = webdriver.Firefox()
    page_number = 1
    print("----- Scraping CPU -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[88]/input"
    driver.get(url)
    select_category(driver, xpath_complete) 
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_cpu(driver, actual_url) 
        page_number += 1
        all_components.extend(data_scrapped)
        # input("Press Enter to continue...")
        if not data_scrapped:
            break

    print("----- Scraping GPU -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[126]/input"
    driver.get(url)
    xpath_complete_subcategory = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[5]/div/div/label[2]/input"
    select_category(driver, xpath_complete, subcategory=xpath_complete_subcategory)
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    page_number = 1
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_gpu(driver, actual_url)
        all_components.extend(data_scrapped)    
        page_number += 1
        if not data_scrapped:
            break

    print("----- Scraping Motherboard -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[114]/input"
    driver.get(url)
    select_category(driver, xpath_complete)
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    page_number = 1
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_mb(driver, actual_url)
        all_components.extend(data_scrapped)
        page_number += 1
        if not data_scrapped:
            break

    print("----- Scraping Gabinete -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[42]/input"
    driver.get(url)
    select_category(driver, xpath_complete)
    WebDriverWait(driver, 90).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    page_number = 1
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_gab(driver, actual_url)
        all_components.extend(data_scrapped)
        page_number += 1
        if not data_scrapped:
            break

    print("----- Scraping PSU -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[34]/input"
    driver.get(url)
    xpath_complete_subcategory = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[5]/div/div/label[7]/input"
    select_category(driver, xpath_complete, subcategory=xpath_complete_subcategory)
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    page_number = 1
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_psu(driver, actual_url)
        all_components.extend(data_scrapped)    
        page_number += 1
        if not data_scrapped:
            break

    print("----- Scraping Enfriamiento Liquido -----")
    xpath_complete = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[4]/div/div/label[125]/input"
    driver.get(url)
    xpath_complete_subcategory = "/html/body/main/aside/div/div/div/div[2]/div/div/div/form/div[5]/div/div/label[2]/input"
    select_category(driver, xpath_complete, subcategory=xpath_complete_subcategory)
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'get-pedidos')))
    page_number = 1
    while True:
        actual_url = f"{url_scraped}{page_number}"
        print(actual_url)
        time.sleep(3)
        data_scrapped = scrape_cooler(driver, actual_url)
        all_components.extend(data_scrapped)    
        page_number += 1
        if not data_scrapped:
            break

    clean_data = []
    existing_codes = set()
    for component in all_components:
        if component["cp"] not in existing_codes:
            clean_data.append([
                component["category"], 
                component["code"], 
                component["cp"], 
                component["description"], 
                component["brand"], 
                component["obtained_from"], 
                component["existence"],
                component["price"]
            ])
            existing_codes.add(component["cp"])
        else:
            pass
    
    driver.quit()    


    df = pd.DataFrame(clean_data, columns=['Categoria', 'SKU', 'Codigo Propietario', 'Titulo', 'Marca', 'Proveedor', 'Stock', 'Costo'])

    print(df)

    df.to_excel('data.xlsx', index=False)
    print("Información de CVA actualizada con éxito!")