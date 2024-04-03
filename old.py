from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys




page_to_scrape = requests.get("https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
categorias = "CPU"

skus = soup.findAll("div", attrs={"class":"emproduct_right_artnum"})
lista_skus = []
for sku in skus:
    lista_skus.append(sku.text)

prices = soup.findAll("label", attrs={"class":"price"})
lista_prices = []
for price in prices:
    lista_prices.append(price.text)


titles = []
for x in range(17):
    temps = soup.findAll("a", attrs={"id":f"productList-{x+1}"})
    for y in temps:
        texto = y.text
        titles.append(texto)
titulos = []
for dato in titles:
    titulos.append(dato.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    
emstock_divs = soup.findAll("div", class_="emstock")
stock = []
for div in emstock_divs:
    span = div.find("span")
    if span:
        stock.append(span.text.strip())


data = []
for x in range(len(titulos)):
    temp_list = []  # Create a temporary list to store data for each iteration
    temp_list.append(categorias)
    temp_list.append(lista_skus[x])
    temp_list.append(titulos[x])
    if "AMD" in titulos[x]:
        temp_list.append("AMD")
    elif "Intel" in titulos[x]:
        temp_list.append("INTEL")
    temp_list.append("Cyberpuerta")
    temp_list.append(stock[x])
    temp_list.append(lista_prices[x])
    data.append(temp_list) 


data_tuple = tuple(data)

df = pd.DataFrame(data_tuple, columns=['Categoria','SKU','Titulo','Marca','Proveedor','Stock','Costo'])

df.to_excel('database.xlsx', index = False)