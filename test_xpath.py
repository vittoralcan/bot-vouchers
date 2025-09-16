from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

# 1. Configurar o driver do navegador
# Substitua o caminho abaixo pelo caminho do seu chromedriver
# Você pode fazer o download do chromedriver aqui: https://chromedriver.chromium.org/downloads
# Se o seu driver estiver no PATH do sistema, esta linha não é necessária
driver = webdriver.Chrome()

# 2. Abrir a página web
# Substitua esta URL pela página que você deseja automatizar
url = "https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm"
driver.get(url)

time.sleep(2)  # Espera a página carregar

# Preencher os campos de login
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input').click()
time.sleep(1)

pyautogui.write('6696')
pyautogui.press('tab')
pyautogui.write('32901548000107')
time.sleep(1)

driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button').click()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input').click()
time.sleep(2)

# 3. Localizar o elemento usando o XPath e extrair o texto
# Substitua este XPath pelo XPath do elemento que você precisa
    xpath = "/html/body/div[5]/div/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[2]" # Exemplo: Localiza o título principal da página



    # 4. Exibir o texto no terminal
 