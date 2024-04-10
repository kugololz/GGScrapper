# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import sys




# page_to_scrape = requests.get("https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# categorias = "CPU"

# skus = soup.findAll("div", attrs={"class":"emproduct_right_artnum"})
# lista_skus = []
# for sku in skus:
#     lista_skus.append(sku.text)

# prices = soup.findAll("label", attrs={"class":"price"})
# lista_prices = []
# for price in prices:
#     lista_prices.append(price.text)


# titles = []
# for x in range(17):
#     temps = soup.findAll("a", attrs={"id":f"productList-{x+1}"})
#     for y in temps:
#         texto = y.text
#         titles.append(texto)
# titulos = []
# for dato in titles:
#     titulos.append(dato.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    
# emstock_divs = soup.findAll("div", class_="emstock")
# stock = []
# for div in emstock_divs:
#     span = div.find("span")
#     if span:
#         stock.append(span.text.strip())


# data = []
# for x in range(len(titulos)):
#     temp_list = []  # Create a temporary list to store data for each iteration
#     temp_list.append(categorias)
#     temp_list.append(lista_skus[x])
#     temp_list.append(titulos[x])
#     if "AMD" in titulos[x]:
#         temp_list.append("AMD")
#     elif "Intel" in titulos[x]:
#         temp_list.append("INTEL")
#     temp_list.append("Cyberpuerta")
#     temp_list.append(stock[x])
#     temp_list.append(lista_prices[x])
#     data.append(temp_list) 


# data_tuple = tuple(data)

# df = pd.DataFrame(data_tuple, columns=['Categoria','SKU','Titulo','Marca','Proveedor','Stock','Costo'])

# df.to_excel('database.xlsx', index = False)

from bs4 import BeautifulSoup

# Assume 'html_content' contains the HTML content you provided
html_content = '''
<div class="mdl-card__stock-section">
    <span class="mdl-card__stock">
        EXIS
        <span class="mdl-card__stock-number">
            4
        </span>
    </span>
    <span class="mdl-card__stock">
        TRANS
        <span class="mdl-card__stock-number">
            1
        </span>
    </span>
    <span class="mdl-card__stock">
        EXIS FUT
        <span class="mdl-card__stock-number">
            5
        </span>
    </span>
    <span class="mdl-card__stock">
        EXIST CD
        <span class="mdl-card__stock-number">
            1632
        </span>
    </span>
    <span class="mdl-card__stock px-0" style="border-radius: 0px;">
        <a onclick="GLOBAL.openExistencia('existencia-general', '10312616', '1', 'CP-1282', 'https://me2.grupocva.com/me/')" data-balloon="Ver Existencia Sucursales" data-balloon-pos="up" class="show-toggle-sucursales   icon-button-building">
            SUC
        </a>
    </span>
</div>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Custom function to filter span elements based on your criteria
def is_exis_span(element):
    return element.name == 'span' and 'EXIS' in element.get_text()

# Find the span element containing "EXIS" and the numeric value following it
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

    print("EXIS:", exis_text.strip())
    print("Numeric value:", numeric_value.strip())
else:
    print("No span element containing 'EXIS' found")



