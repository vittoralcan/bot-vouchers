import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def comparar_texto_xpath_com_clipboard(url, xpath):
    """
    Compara o texto de um elemento localizado por XPath com o texto da área de transferência.

    Args:
        url (str): A URL da página web a ser acessada.
        xpath (str): O XPath do elemento que contém o texto a ser comparado.
    """
    driver = None
    try:
        # Inicializa o driver do Chrome
        driver = webdriver.Chrome()

        # Acessa a URL da página web
        driver.get('https://www.unisystemtec.com.br/portal_socio/index.php?class=PedidoConvite')

        # 1. Obtém o texto da área de transferência (clipboard)
        texto_clipboard = pyperclip.paste()
        print(f"Texto do Clipboard: '{texto_clipboard}'")

        # 2. Localiza o elemento usando o XPath
        elemento = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[3]/div[1]/div')

        # 3. Obtém o texto do elemento
        texto_elemento = elemento.text
        print(f"Texto do Elemento na Web: '{texto_elemento}'")

        # 4. Compara os dois textos
        if texto_elemento == texto_clipboard:
            print("\n✅ O texto do elemento na web é IGUAL ao texto da área de transferência.")
        else:
            print("\n❌ O texto do elemento na web é DIFERENTE do texto da área de transferência.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        print("Finalizando o driver...")
        if driver:
            driver.quit()

# --- Exemplo de uso ---
if __name__ == "__main__":
    # Substitua a URL e o XPath pelos valores desejados
    # IMPORTANTE: Você deve ter o texto a ser comparado já copiado para o clipboard
    url_do_site = "https://www.google.com" # Exemplo, substitua pela URL real
    xpath_do_elemento = "//*[@id='nome_do_elemento']" # Exemplo, substitua pelo XPath real

    comparar_texto_xpath_com_clipboard(url_do_site, xpath_do_elemento)

    