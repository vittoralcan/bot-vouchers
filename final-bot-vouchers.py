from selenium import webdriver #lautomação do navegador
from selenium.webdriver.common.by import By #localização de elementos
import pyautogui #automação do teclado e mouse
import time #tempo de espera
import pyperclip #manipulação da área de transferência
import os #interação com o sistema operacional
from selenium.webdriver.support.ui import WebDriverWait #esperas explícitas
from selenium.webdriver.support import expected_conditions as EC #condições para esperas explícitas
import datetime #manipulação de datas
import sys #manipulação de sistema

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
                navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input').send_keys(campo_usuario)
            
            if campo_senha:
                navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input').send_keys(campo_senha)
                
            time.sleep(4)
            
            #caminho para chegar no preenchimento    
            navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button').click()
            
            time.sleep(12)
            
            
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a').click()
            time.sleep(4)
            
            navegador.find_element(By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a').click()
            
            time.sleep(7)
            
            navegador.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[2]/div/input').click()
            time.sleep(4)
            
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
            
            #1 - Pega o texto da área de transferência converte e salva em um arquivo -------------------------------------------------

     
            def converter_mes_e_salvar():
                """
                1. Pega a data da área de transferência (clipboard) no formato DD/MM/AAAA.
                2. Converte o número do mês para o nome do mês em português.
                3. Salva o resultado no arquivo 'data_cliente.txt'.
                """
                try:
                    # Pega a data da área de transferência
                    data_string = pyperclip.paste()
                    
                    # Dicionário de conversão de números para nomes de meses
                    nomes_meses = {
                        1: "JANEIRO", 2: "FEVEREIRO", 3: "MARÇO", 4: "ABRIL",
                        5: "MAIO", 6: "JUNHO", 7: "JULHO", 8: "AGOSTO",
                        9: "SETEMBRO", 10: "OUTUBRO", 11: "NOVEMBRO", 12: "DEZEMBRO"
                    }

                    # Converte a string da data para um objeto de data
                    data_objeto = datetime.datetime.strptime(data_string, '%d/%m/%Y')
                    
                    # Extrai o número do mês e o ano
                    mes_numero = data_objeto.month
                    ano = data_objeto.year
                    
                    # Encontra o nome do mês usando o dicionário
                    mes_nome = nomes_meses.get(mes_numero)

                    if mes_nome:
                        # Formata a string final no formato "MÊS ANO"
                        resultado = f"{mes_nome} {ano}"
                        caminho_arquivo = "data_cliente.txt"
                        
                        # Cria ou sobrescreve o arquivo e salva o resultado
                        # O 'with open(...)' garante que o arquivo será fechado automaticamente
                        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                            arquivo.write(resultado)
                        
                        print(f"Sucesso! O texto '{resultado}' foi salvo no arquivo '{caminho_arquivo}'.")
                    else:
                        print("Erro: O número do mês na data não é válido.")

                except ValueError:
                    print("Erro: A data na área de transferência não está no formato DD/MM/AAAA.")
                except pyperclip.PyperclipException:
                    print("Erro: A biblioteca 'pyperclip' não conseguiu acessar a área de transferência. Certifique-se de que ela está instalada e que o sistema suporta.")
                except Exception as e:
                    print(f"Ocorreu um erro inesperado: {e}")

            # --- Chamada da função para executar o código ---
            if __name__ == "__main__":
                converter_mes_e_salvar()

            #2 - Lê o texto encontrado dentro do xpath --------------------------------------------------------------------------------------------
            
            # O código a seguir assume que a variável 'navegador' já está inicializada
            # Por exemplo: navegador = webdriver.Chrome()

            # Encontra o elemento e lê o texto
            elemento = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[3]/div[1]/div')
            texto_lido = elemento.text

            # Exibe o texto no terminal
            print(f"Texto lido: {texto_lido}")

            # --- Novo bloco de código para salvar o texto em um arquivo .txt ---

            # Define o nome do arquivo
            nome_arquivo = "data_site.txt"

            # Abre o arquivo em modo de escrita ('w') e salva o texto
            # A instrução 'with open(...)' garante que o arquivo será fechado corretamente
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(texto_lido)

            print(f"Texto salvo em {nome_arquivo}")

            # Fim da operação


            #3 - Compara o texto lido com o texto convertido --------------------------------------------------------------------------------------
            
            
            
              

           

            
         

            #------------------------------------------------------------------------------------------------------      
#finalização do código
        except Exception as e:
            print(f"Automação finalizada: {e}")
                 
print("Automação concluída.")






time.sleep(4)

navegador.quit()
