from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui
import pyautogui
import pyperclip
import os
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime

#----------------- LEITURA DE ID DE HORÁRIO DA PLANILHA ------------------#

navegador = webdriver.Chrome()

navegador.get("https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408")

time.sleep(2)

#pressiona seta para baixo
pyautogui.press('down')

#copia o texto selecionado
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

#----------------- Automação com Verificação de ID -------------------#

def verificar_e_salvar_id(novo_id):
    """
    Verifica se o novo ID é igual ao ID salvo no arquivo.
    Se for igual, retorna False.
    Se for diferente, salva o novo ID e retorna True.
    """
    nome_arquivo = "last_time"
    
    id_salvo = ""
    # Tenta ler o ID salvo do arquivo
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            id_salvo = arquivo.read().strip()
    
    # Compara os IDs
    if novo_id == id_salvo:
        print(f"ID '{novo_id}' já foi processado. Encerrando a automação.")
        return False
    else:
        # Se for um novo ID, salva no arquivo
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(novo_id)
        print(f"Novo ID '{novo_id}' detectado. Prosseguindo com automação...")
        return True

def executar_resto_da_automacao():
    """
    Aqui vai o seu código da automação que deve ser executado
    apenas quando o ID é novo.
    """
    print("Executando o restante da sua automação...")
    
    # Adicione aqui o seu código PyAutoGUI e/ou Selenium.
    # Por exemplo:
    # pyautogui.click(x=100, y=200)
    # pyautogui.write("Olá Mundo")
    # driver.get("https://outra-pagina.com")
    
    time.sleep(5) # Apenas para simular a execução
    
    print("Automação concluída.")

def main():
    """
    Função principal que orquestra a automação a partir do ID na área de transferência.
    """
    print("Verificando a área de transferência...")
    
    # Pega o texto da área de transferência
    id_copiado = pyperclip.paste().strip()
    
    if not id_copiado:
        print("Erro: A área de transferência está vazia. Não há ID para comparar.")
        return
        
    print(f"ID lido da área de transferência: '{id_copiado}'")

    # Chama a função de verificação
    if verificar_e_salvar_id(id_copiado):
        # Se a função retornar True, o ID é novo, então executa o resto do código
        

#--------- PREENCHIMENTO NO NAVEGADOR APÓS COLETA DE DADOS -------------#
        
        
        executar_resto_da_automacao()
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
            time.sleep(2)
            
            #login dentro do site UniSystem
            if campo_usuario:
                navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input').send_keys(campo_usuario)
            
            if campo_senha:
                navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input').send_keys(campo_senha)
                
            time.sleep(2)
            
            #caminho para chegar no preenchimento    
            navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button').click()
            
            time.sleep(5)
            
            
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
            time.sleep(2)
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
            
            time.sleep(2)
            
            navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[2]/div/input').click()
            time.sleep(2)
            
            #abre a janela da planilha
            navegador.execute_script("window.open('https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408', '_blank');")
            time.sleep(10)
            
            #pega o ID da planilha
            pyautogui.press('down')
            pyautogui.press('right')
            time.sleep(1)
            
            #copia o ID da planilha
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            #volta para a janela do navegador
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            #cola o ID na caixa de texto
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            
            #volta para a janela do navegador
            time.sleep(1)
            pyautogui.press('right')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            #cola o ID na caixa de texto
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            pyautogui.press('right')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            pyautogui.hotkey('space')
            time.sleep(1)
            
            pyautogui.hotkey('down')
            pyautogui.hotkey('enter')
            time.sleep(1)
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            pyautogui.press('right')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            pyautogui.hotkey('enter')
            time.sleep(1)
            
            navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input').click()
            time.sleep(1)
            
            pyautogui.hotkey('ctrl','tab')
            time.sleep(1)
            
            pyautogui.press('right')
            pyautogui.hotkey('ctrl','c')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl','tab')
            time.sleep(1)
            
            pyautogui.hotkey('ctrl','v')
            time.sleep(1)

            navegador.find_element(By.XPATH,'/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input')
            time.sleep(5)
            
            print("Automação concluída.")
            

        except NoSuchElementException:
            print("Um ou mais elementos não foram encontrados na página.")
        except Exception as e:
            print(f"Ocorreu um erro durante a automação: {e}")
        finally:
            #aguardar 10s antes de fechar o navegador
            time.sleep(10)
            navegador.quit()
    
    else:
        # Se a função retornar False, o ID é repetido, e o script termina.
        pass

if __name__ == "__main__":
    main()
    

