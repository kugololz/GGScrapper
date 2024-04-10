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
    

    
    
    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    login(driver)
    driver.close()