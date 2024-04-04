import requests
from bs4 import BeautifulSoup

login_url = 'https://covirsast.com/site/login-sesion'
username = 'compras@grupordc.com.mx'
password = '123'

login_data = {
    'usuario': username,
    'contraseña': password
}

session = requests.Session()

res = session.post(login_url, data = login_data)

if res.status_code == 200:
    print('Inicio de sesión correcto')
else:
    print("Error al iniciar sesion")
