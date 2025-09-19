from selenium import webdriver #lautomação do navegador
from selenium.webdriver.common.by import By #localização de elementos
import pyautogui #automação do teclado e mouse
import time #tempo de espera
import pyperclip #manipulação da área de transferência
import os #interação com o sistema operacional
from selenium.webdriver.support.ui import WebDriverWait #esperas explícitas
from selenium.webdriver.support import expected_conditions as EC #condições para esperas explícitas

# - Section 1 - Abrir o navegador 
navegador=webdriver.Chrome()

navegador.get('https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408')
time.sleep(4)

pyautogui.press("down")
time.sleep(1)
pyautogui.hotkey('ctrl','c')

def ler_e_imprimir_clipboard(): 
#Lê o conteúdo da área de transferência e o apresenta no terminal.
    try:
        conteudo = pyperclip.paste()
        print("Conteúdo da área de transferência:")
        print(conteudo)
    except pyperclip.PyperclipException as e:
        print(f"Não foi possível acessar a área de transferência. Erro: {e}")

if __name__ == "__main__":
    ler_e_imprimir_clipboard()
time.sleep(2) 
#próximo passo.

import pyperclip
import os

def ler_conteudo_do_arquivo():
    # Caminho do arquivo de texto
    caminho_do_arquivo = r"D:\\Projetos\\Tesseratto\\PROJETO - SEICON-DF\\automations\\bot-vouchers\\last_time.txt"
    
    # Adicionamos uma verificação simples para verificar se o caminho existe.
    if not os.path.exists(caminho_do_arquivo):
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        # Retorna uma string vazia para evitar erros na comparação.
        return ""
    
    print("\n Lendo o conteúdo do arquivo")
    try:
        # 'with' usado para garantir que o arquivo seja fechado automaticamente.
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo lido:")
            print(conteudo)

            return conteudo
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
        # Retornamos uma string vazia em caso de erro na leitura
        return ""

# --- Parte principal da automação ---
if __name__ == "__main__":
    # Pega o texto da área de transferência
    texto_area_transferencia = pyperclip.paste()
    
    # Pega o texto do arquivo usando a função que criamos
    texto_bloco_notas = ler_conteudo_do_arquivo()
    
    # Realiza a comparação
    if texto_area_transferencia == texto_bloco_notas:
        print("Os textos são idênticos. Encerrando a automação.")
    else:
        print("Os textos são diferentes. Continuando com a automação.")
        # Automação de preenchimento das informações
        time.sleep(2)
        #--------- PREENCHIMENTO NO NAVEGADOR APÓS COLETA DE DADOS -------------#
                    # Acessar o site
        navegador.get("https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm")
        time.sleep(1)
        navegador.maximize_window()
        time.sleep(1)

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
                navegador.finlement(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input').send_keys(campo_usuario)
            
            if campo_senha:
                navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input').send_keys(campo_senha)
                
            time.sleep(4)
            
            #caminho para chegar no preenchimento    
            navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button').click()
            
            time.sleep(1)
            
            
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
            time.sleep(1)
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
            
            time.sleep(1)
            
            navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[2]/div/input').click()
            time.sleep(2)
            
            #abre a janela da planilha
            navegador.execute_script("window.open('https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408', '_blank');")
            time.sleep(3)
            
            #Preencher NOME
            pyautogui.press('down') #econtra ID
            pyautogui.press('right')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')   #copia o ID 
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')  #volta para a janela do navegador
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')   #cola o ID 
            time.sleep(1)

         
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            # Preencher EMAIL.
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.press('right') #encontra email.
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')  #copia e-mail.
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v') #cola o e-mail.
            time.sleep(1)

            pyautogui.hotkey('tab')
            time.sleep(1)
            
            #Preechimento DATA DE NASCIMENTO
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.press('right')
            pyautogui.hotkey('ctrl', 'c') #copia a data de nascimento
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v') #cola a data de nascimento
            time.sleep(1)
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            #Preechimento CPF pt.1
            pyautogui.hotkey('space')
            time.sleep(1)
            pyautogui.hotkey('down') #seleciona o campo CPF
            pyautogui.hotkey('enter')
            time.sleep(1)
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            
            #Preechimento CPF pt.2
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.press('right')
            pyautogui.hotkey('ctrl', 'c') #copia o CPF
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v') #cola o CPF
            time.sleep(1)

            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)

            #Seleciona a DATA DE VISITA AO CLUBE      
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.hotkey('ctrl', 'c') #copia a data de visita ao clube
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(1)

            #selecionar data de visita ao clube
            navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input').click()
            time.sleep(2)
            
           

           #Tabela comparativa de data de visita ao clube ----------------------------------------
            
            

            
         

            #------------------------------------------------------------------------------------------------------      
#finalização do código
        except Exception as e:
            print(f"Automação finalizada: {e}")
                 
print("Automação concluída.")






time.sleep(4)

navegador.quit()
