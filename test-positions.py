from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pyautogui

def testar_leitura_xpath(url, xpath_do_elemento):
    """
    Função para testar a leitura do texto de um elemento por XPath.

    Args:
        url (str): A URL da página web a ser acessada.
        xpath_do_elemento (str): O XPath do elemento que você quer ler.
    """
    driver = None
    try:
        # Inicializa o serviço do ChromeDriver
        # Substitua o caminho do serviço se necessário
        service = Service('caminho/para/chromedriver')
        driver = webdriver.Chrome(service=service)
        
        # Acessa a página web
        driver.get('https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm')

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input')
        pyautogui.write('6696')

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input')
        pyautogui.write('32901548000107')

        driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div/ul/li[3]/a').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div/ul/li[3]/a').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div/ul/li[3]/a').click()
        time.sleep(4)
        # Aguarda um tempo para a página carregar completamente
        time.sleep(7) 

        driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input').click()
        time.sleep(4)


        
        # Encontra o elemento usando o XPath
        elemento = driver.find_element(By.XPATH, ' /html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input')
        
        # Obtém o texto do elemento
        texto_lido = elemento.text
        
        # Imprime o texto lido no terminal
        print("--- Resultado da Leitura do XPath ---")
        print(f"URL: {url}")
        print(f"XPath de teste: {xpath_do_elemento}")
        print(f"Texto lido: '{texto_lido}'")
        print("-----------------------------------")
        
    except Exception as e:
        print(f"Ocorreu um erro: Não foi possível ler o elemento. Verifique se o XPath está correto ou se o elemento já carregou na página.")
        print(f"Erro: {e}")
        
    finally:
        if driver:
            driver.quit()

# --- Configurações de Teste ---
# 1. Substitua esta URL pela URL da sua página
url_da_pagina = "https://www.exemplo.com" 

# 2. Substitua este XPath pelo XPath que você quer testar
# Por exemplo: "//div[contains(@class, 'red-bg')]//div[contains(@class, 'title')]"
xpath_para_testar = "COLE_SEU_XPATH_AQUI" 

# --- Executa o Teste ---
testar_leitura_xpath(url_da_pagina, xpath_para_testar)