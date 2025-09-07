from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 1. Configurar o driver do navegador
# Substitua o caminho abaixo pelo caminho do seu chromedriver
# Você pode fazer o download do chromedriver aqui: https://chromedriver.chromium.org/downloads
# Se o seu driver estiver no PATH do sistema, esta linha não é necessária
driver = webdriver.Chrome()

# 2. Abrir a página web
# Substitua esta URL pela página que você deseja automatizar
url = "https://github.com/vittoralcan"
driver.get(url)

# 3. Localizar o elemento usando o XPath e extrair o texto
# Substitua este XPath pelo XPath do elemento que você precisa
try:
    xpath = "/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]" # Exemplo: Localiza o título principal da página
    elemento = driver.find_element(By.XPATH, xpath)
    texto_extraido = elemento.text

    # 4. Exibir o texto no terminal
    print("Texto encontrado no XPath '{}':".format(xpath))
    print("---------------------------------")
    print(texto_extraido)
    print("---------------------------------")

except Exception as e:
    print(f"Erro ao encontrar o elemento ou extrair o texto: {e}")

finally:
    # 5. Fechar o navegador no final
    driver.quit()