from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui
#--------------------"DISPARAGEM" DE AUTOMAÇÃO -----------------------#



#------------------ ABERTURA DO GOOGLE FORMS -------------------#

#abrir o navegador
navegador = webdriver.Chrome()

# Acessar o site
navegador.get("https://docs.google.com/forms/d/1R_ppy0-ZmkPu_U-J4hzj6Ga1IlpWVGBZndlT1ZHLn00/edit")

#colocar navegador em tela cheia
navegador.maximize_window()

#Espera a página carregar
time.sleep(5)

#clica em respostas
pyautogui.press('esc')
time.sleep(5)

#clica em respostas
pyautogui.click(934, 342)
time.sleep(5)

#-------------------- FILTRO DE DADOS DO FORMS -----------------------#



#------------------ RECOLHIMENTO DE DADOS DA PLANILHA -------------------#



#--------- PREENCHIMENTO NO NAVEGADOR APÓS COLETA DE DADOS -------------#

# Acessar o site
navegador.get("https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm")

#colocar navegador em tela cheia
navegador.maximize_window()

# Exemplo de dados fictícios para teste
dados = {
    "Usuario": "6696",
    "Senha": "32901548000107"
}

try:
    # Exemplo de como usar os dados para preencher campos
    # Note que os nomes das chaves devem ser iguais aos cabeçalhos da sua planilha
    campo_usuario = dados.get("Usuario")
    campo_senha = dados.get("Senha")
    
    #login dentro do site UniSystem
    if campo_usuario:
        navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input').send_keys(campo_usuario)
    
    if campo_senha:
        navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input').send_keys(campo_senha)
        
    time.sleep(2)
    
    #caminho para chegar no preenchimento    
    navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button').click()
    
    time.sleep(2)
    
    
    
    navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
    
    navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
    
    time.sleep(2)
    
    navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[2]/div/input').click()

    print("Dados da primeira linha preenchidos com sucesso!")
    

except NoSuchElementException:
    print("Um ou mais elementos não foram encontrados na página.")
except Exception as e:
    print(f"Ocorreu um erro durante a automação: {e}")
finally:
    #aguardar 10s antes de fechar o navegador
    time.sleep(10)
    navegador.quit()