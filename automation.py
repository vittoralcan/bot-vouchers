import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager 
import locale
import pyautogui
import threading
import tkinter as tk
from tkinter import scrolledtext

# Variáveis do Tkinter
running = False 
# Variável para armazenar a instância da janela principal do Tkinter
root = None 
# Variável para a área de log
log_area = None 
# Variável para a instância do WebDriver
driver = None 

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
RANGE = 'dados_ordenados!A2:X2' 
SAMPLE_SPREADSHEET_ID = '1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8'
ID_FILE = "last_processed_id.txt"


def log_message(message):
    """Direciona as mensagens para a área de log da GUI."""
    if log_area:
        # Insere a mensagem e rola automaticamente para o final
        log_area.insert(tk.END, f"{datetime.now().strftime('%H:%M:%S')} - {message}\n")
        log_area.see(tk.END)
    else:
        # Mantém o print no console como fallback
        print(message)


def get_sheet_data():
    """Conecta à API do Google Sheets e retorna os dados da última linha."""
    global running
    
    if not running:
        log_message("Interrompido. Pulando a busca de dados.")
        return None, None
        
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'cred.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    log_message('Conectado ao Google Sheets API com sucesso.')

    sheet = service.spreadsheets()
    try:
        result = sheet.values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=RANGE
        ).execute()
    except Exception as e:
        log_message(f"Erro ao ler a planilha: {e}")
        return None, None
        
    values = result.get('values', [])

    if not values:
        log_message("Erro: Nenhum dado encontrado na planilha. Encerrando automação.")
        return None, None

    latest_row = values[-1]

    try:
        new_id = latest_row[0] 
    except IndexError:
        log_message("Erro: A última linha da planilha está vazia ou incompleta. Encerrando automação.")
        return None, None

    # Lê o último ID processado do arquivo
    last_id = None
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as f:
            last_id = f.read().strip()
    
    # Compara os IDs e decide se continua ou encerra
    if new_id == last_id:
        log_message(f"Atenção: O ID {new_id} já foi processado. Aguardando próximo ciclo.")
        return None, None
    else:
        log_message(f"Novo ID encontrado ({new_id})! Iniciando processamento...")
        
        row_data = latest_row
        
        # Cria um dicionário com todos os dados lidos
        data = {
            'id': row_data[0] if len(row_data) > 0 else None,
            'name': row_data[1] if len(row_data) > 1 else None,
            'email': row_data[2] if len(row_data) > 2 else None,
            'birth': row_data[3] if len(row_data) > 3 else None,
            'cpf': row_data[4] if len(row_data) > 4 else None,
            'condominio': row_data[5] if len(row_data) > 5 else None,
            'data_visita': row_data[6] if len(row_data) > 6 else None,
            # Acompanhantes
            'acomp1_nome': row_data[8] if len(row_data) > 8 else None,
            'acomp1_parentesco': row_data[9] if len(row_data) > 9 else None,
            'acomp1_nasc': row_data[10] if len(row_data) > 10 else None,
            'acomp1_cpf': row_data[11] if len(row_data) > 11 else None,
            'acomp2_nome': row_data[12] if len(row_data) > 12 else None,
            'acomp2_parentesco': row_data[13] if len(row_data) > 13 else None,
            'acomp2_nasc': row_data[14] if len(row_data) > 14 else None,
            'acomp2_cpf': row_data[15] if len(row_data) > 15 else None,
            'acomp3_nome': row_data[16] if len(row_data) > 16 else None,
            'acomp3_parentesco': row_data[17] if len(row_data) > 17 else None,
            'acomp3_nasc': row_data[18] if len(row_data) > 18 else None,
            'acomp3_cpf': row_data[19] if len(row_data) > 19 else None,
            'acomp4_nome': row_data[20] if len(row_data) > 20 else None,
            'acomp4_parentesco': row_data[21] if len(row_data) > 21 else None,
            'acomp4_nasc': row_data[22] if len(row_data) > 22 else None,
            'acomp4_cpf': row_data[23] if len(row_data) > 23 else None,
        }
        
        # Salva o novo ID para a próxima execução
        with open(ID_FILE, "w") as f:
            f.write(new_id)
        
        return data, new_id


def fill_dependents_form(driver, wait, data):
    """
    Função para iterar e preencher o formulário modal de Adicionar Dependente
    para até 4 acompanhantes.
    """
    global running
    log_message("\n--- Iniciando Preenchimento dos Acompanhantes ---")
    
    dependents = [
        {'nome': data.get('acomp1_nome'), 'parentesco': data.get('acomp1_parentesco'), 'nasc': data.get('acomp1_nasc'), 'cpf': data.get('acomp1_cpf')},
        {'nome': data.get('acomp2_nome'), 'parentesco': data.get('acomp2_parentesco'), 'nasc': data.get('acomp2_nasc'), 'cpf': data.get('acomp2_cpf')},
        {'nome': data.get('acomp3_nome'), 'parentesco': data.get('acomp3_parentesco'), 'nasc': data.get('acomp3_nasc'), 'cpf': data.get('acomp3_cpf')},
        {'nome': data.get('acomp4_nome'), 'parentesco': data.get('acomp4_parentesco'), 'nasc': data.get('acomp4_nasc'), 'cpf': data.get('acomp4_cpf')},
    ]

    # XPATHs fixos
    ADD_DEPENDENT_BUTTON = "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[10]/div/div/div/div/table/tbody/tr/td[3]/i"
    CLOSE_MODAL_BUTTON = "/html/body/div[5]/div[1]/button"
    SAVE_MODAL_BUTTON = "/html/body/div[5]/div[2]/div/div[2]/button"
    
    # XPATHs dentro do modal (div[5])
    NOME_INPUT = "/html/body/div[5]/div[2]/div/div[1]/div/form/div/div/div/div[1]/div[2]/div/input"
    PARENTESCO_SELECT = "/html/body/div[5]/div[2]/div/div[1]/div/form/div/div/div/div[1]/div[4]/div/select"
    DATA_NASC_INPUT = "/html/body/div[5]/div[2]/div/div[1]/div/form/div/div/div/div[2]/div[2]/div/input"
    TIPO_DOC_SELECT = "/html/body/div[5]/div[2]/div/div[1]/div/form/div/div/div/div[2]/div[4]/div/select"
    NUMERO_DOC_INPUT = "/html/body/div[5]/div[2]/div/div[1]/div/form/div/div/div/div[2]/div[5]/div/input"

    for i, acomp in enumerate(dependents):
        if not running:
            log_message("Interrupção solicitada. Parando preenchimento de dependentes.")
            break

        acomp_num = i + 1
        nome = acomp['nome']
        parentesco = acomp['parentesco']
        data_nasc = acomp['nasc']
        cpf = acomp['cpf']
        
        log_message(f"\n-> Processando Acompanhante {acomp_num}...")

        if not nome or nome.strip() == "":
            log_message(f"Nome do Acompanhante {acomp_num} está vazio. Finalizando preenchimento de dependentes.")
            try:
                # Tenta abrir e fechar o modal para garantir o estado
                wait.until(EC.element_to_be_clickable((By.XPATH, ADD_DEPENDENT_BUTTON))).click()
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, CLOSE_MODAL_BUTTON))).click()
                log_message("Modal fechado.")
            except:
                 pass
            break

        log_message(f"Dados encontrados: Nome='{nome}', Parentesco='{parentesco}', CPF='{cpf}'")

        try:
            # 1. Abrir o modal de Adicionar Dependente
            wait.until(EC.element_to_be_clickable((By.XPATH, ADD_DEPENDENT_BUTTON))).click()
            log_message("Modal aberto. Aguardando estabilização...")
            time.sleep(1)
            
            # 2. Espera que o primeiro campo de texto (Nome) APAREÇA no modal
            wait.until(EC.presence_of_element_located((By.XPATH, NOME_INPUT)))
            
            # 3. Preencher o Nome do Convidado
            driver.find_element(By.XPATH, NOME_INPUT).send_keys(nome)
            
            # 4. Selecionar o Grau de Parentesco
            select_parentesco_element = wait.until(EC.presence_of_element_located((By.XPATH, PARENTESCO_SELECT)))
            select_parentesco = Select(select_parentesco_element)
            select_parentesco.select_by_visible_text(parentesco.upper())
            time.sleep(0.5)

            # 5. Preencher a Data de Nascimento
            driver.find_element(By.XPATH, DATA_NASC_INPUT).send_keys(data_nasc)
            time.sleep(0.5)

            # 6. Selecionar o Tipo de Documento "CPF"
            select_doc_element = wait.until(EC.presence_of_element_located((By.XPATH, TIPO_DOC_SELECT)))
            select_doc_element.click() 
            time.sleep(0.5)
            
            # Usando pyautogui para selecionar a segunda opção (CPF)
            pyautogui.press('down') 
            pyautogui.press('enter')
            time.sleep(1)

            # Pausa de 2 segundos
            time.sleep(2)

            # 7. Preencher o CPF 
            driver.find_element(By.XPATH, NUMERO_DOC_INPUT).send_keys(cpf)
            time.sleep(1)

            # 8. Clicar em Salvar 
            wait.until(EC.element_to_be_clickable((By.XPATH, SAVE_MODAL_BUTTON))).click()
            log_message(f"Acompanhante {acomp_num} - **{nome}** salvo com sucesso!")
            time.sleep(1) 
            
            # 9. Clicar em Fechar o Modal
            wait.until(EC.element_to_be_clickable((By.XPATH, CLOSE_MODAL_BUTTON))).click()
            log_message("Modal de acompanhante fechado.")
            time.sleep(2)
            
        except Exception as e:
            log_message(f"Erro ao preencher Acompanhante {acomp_num}. Tentando fechar modal. Erro: {e}")
            try:
                driver.find_element(By.XPATH, CLOSE_MODAL_BUTTON).click()
                time.sleep(1)
            except:
                pass 
            continue 

    log_message("\nFim do preenchimento de acompanhantes.")


def fill_form_with_selenium(data):
    """Preenche o formulário usando Selenium com os dados da planilha."""
    global running, driver
    
    log_message("Iniciando a automação com Selenium...")

    try:
        # Configura o locale (pode falhar em alguns sistemas, então usamos try/except)
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
    except:
        pass 

    try:
        # Bloco de iniciação do Webdriver manager
        if driver is None:
            # Inicializa o driver. O ChromeDriverManager garante que o driver correto seja baixado/usado.
            log_message("Inicializando WebDriver via ChromeDriverManager...")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            log_message("WebDriver inicializado com sucesso.")
            
        wait = WebDriverWait(driver, 20)
        # Fim do bloco web manager

        log_message("Navegando para a tela de login...")
        driver.get("https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm")
        
        # Preenche o usuário e a senha
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input"))).send_keys("6696")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[2]/div/div[2]/input").send_keys("32901548000107")
        
        # Clica no botão de entrar
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/div[2]/button").click()
        log_message("Login realizado com sucesso.")
        time.sleep(3) 

        # SEGUNDA IMAGEM: Navegação para a página de Convites
        log_message("Navegando para a página de 'Pedidos de Convites'...")
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/aside/div[2]/div/ul/li[4]/a"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a"))).click()
        time.sleep(3)
        
        log_message("Preenchendo o formulário principal...")
        
        # Preenche os dados do titular
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[2]/div/input"))).send_keys(data['name'])
        driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[6]/div[4]/div/input").send_keys(data['email'])
        driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[7]/div[2]/div/input").send_keys(data['birth'])
        
        # Seleção do tipo de documento para CPF
        select_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[7]/div[4]/div/select")))
        Select(select_element).select_by_visible_text("CPF")
        time.sleep(1)
        
        # 4 - CPF
        driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[7]/div[5]/div/input").send_keys(data['cpf'])
        time.sleep(1)
        
        # 5 - Data de Visita (Lógica do Calendário)
        log_message("Selecionando a data de visita no calendário...")
        date_input_xpath = "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input"
        wait.until(EC.presence_of_element_located((By.XPATH, date_input_xpath))).click()
        time.sleep(1)

        parsed_date = datetime.strptime(data['data_visita'], '%d/%m/%Y')
        target_month_year = parsed_date.strftime('%B %Y').upper()
        target_day = str(parsed_date.day)

        current_month_xpath = "/html/body/div[5]/div/div[1]/div[3]/div[1]/div"
        next_month_xpath = "/html/body/div[5]/div/div[1]/div[1]/div[1]/div[3]/a/i"

        while True:
            current_month_element = wait.until(EC.presence_of_element_located((By.XPATH, current_month_xpath)))
            current_month_text = current_month_element.text
            
            if current_month_text.upper() == target_month_year:
                break
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, next_month_xpath))).click()
                time.sleep(0.5) 

        found_day = False
        for row in range(2, 8):
            for col in range(1, 8):
                try:
                    day_xpath = f"/html/body/div[5]/div/div[1]/div[3]/div[1]/table/tbody/tr[{row}]/td[{col}]"
                    day_element = driver.find_element(By.XPATH, day_xpath)
                    
                    if day_element.text == target_day and 'disabled' not in day_element.get_attribute('class'):
                        day_element.click()
                        found_day = True
                        break
                except NoSuchElementException:
                    continue
            if found_day:
                break
        
        if not found_day:
            log_message(f"Erro: Não foi possível encontrar o dia {target_day} no calendário.")
        
        time.sleep(1)
        log_message("Data de visita selecionada.")

        # Simula o tab/enter para fechar o calendário
        driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[7]/div[5]/div/input").click()
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        
        log_message("Formulário principal preenchido.")

        # Processamento de Acompanhantes
        log_message("Aguardando 6 segundos antes de iniciar o preenchimento dos acompanhantes...")
        time.sleep(6) 
        fill_dependents_form(driver, wait, data)

    except WebDriverException as e:
        log_message(f"Erro Crítico ao iniciar o WebDriver: Verifique se o Google Chrome está instalado. Erro: {e}")
        # Definir running=False aqui forçará o loop a parar de forma segura
        global running
        running = False
        return # Sai da função de preenchimento
        
    except Exception as e:
        log_message(f"Ocorreu um erro inesperado durante a automação: {e}")
        
    finally:
        # XPATH do botão Salvar Convite no formulário principal
        SAVE_CONVITE_BUTTON = "/html/body/section[2]/div[1]/div/div/div/div/div/form/div[2]/button[1]"
        
         # Salva o convite apenas se a interrupção não tiver sido solicitada
        if running:
            try:
                log_message("Aguardando 2 segundos antes de salvar o convite final...")
                time.sleep(2)
                
                wait.until(EC.element_to_be_clickable((By.XPATH, SAVE_CONVITE_BUTTON))).click()
                log_message("**Convite final salvo com sucesso!**")
                time.sleep(5) 
            except Exception as e:
                log_message(f"Aviso: Não foi possível clicar no botão 'Salvar Convite' final. Erro: {e}")


# --- Funções de Controle da GUI ---

def automation_loop():
    """Função que roda continuamente enquanto 'running' for True."""
    global running, driver
    log_message("Iniciando loop de automação...")
    
    while running:
        # 1. Tenta obter novos dados da planilha
        data, new_id = get_sheet_data()
        
        if data and running:
            # 2. Se houver novos dados, executa o preenchimento
            fill_form_with_selenium(data)
        
        # 3. Pausa de 1 minuto (60 segundos) antes de checar a planilha novamente
        if running:
            log_message("Ciclo completo. Pausando por 60 segundos antes de checar a planilha novamente...")
            for i in range(60, 0, -1):
                if not running:
                    break
                # Atualiza o log a cada 10 segundos ou menos para não sobrecarregar
                if i % 10 == 0 or i < 5: 
                    log_area.insert(tk.END, f"Aguardando... {i} segundos restantes.\r", 'wait_tag')
                    log_area.see(tk.END)
                time.sleep(1)
            
            # Limpa ou move o cursor para uma nova linha
            log_area.insert(tk.END, "\n", 'wait_tag')
            log_message("Reiniciando a checagem.")
            
    log_message("Loop de automação encerrado.")
    # Fechamento seguro do driver
    if driver:
        try:
            driver.quit()
            driver = None
            log_message("Navegador fechado com sucesso.")
        except Exception as e:
            log_message(f"Erro ao fechar o navegador: {e}")


def start_automation():
    """Lida com o clique no botão Executar."""
    global running
    if not running:
        running = True
        log_message("Execução iniciada.")
        # Inicia a automação em uma thread separada
        threading.Thread(target=automation_loop).start()
    else:
        log_message("A automação já está em execução.")


def stop_automation():
    """Lida com o clique no botão Interromper."""
    global running
    if running:
        running = False
        log_message("Sinal de interrupção enviado. Aguarde o ciclo atual terminar.")
    else:
        log_message("A automação não está em execução.")


def setup_gui():
    """Configura e inicia a interface gráfica (GUI)."""
    global root, log_area
    root = tk.Tk()
    root.title("Controle de Automação de Convites")

    # Frame para os botões
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Botão Executar
    btn_start = tk.Button(button_frame, text="EXECUTAR", command=start_automation, 
                          bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'), width=15)
    btn_start.pack(side=tk.LEFT, padx=10)

    # Botão Interromper
    btn_stop = tk.Button(button_frame, text="INTERROMPER", command=stop_automation, 
                         bg="#F44336", fg="white", font=('Arial', 12, 'bold'), width=15)
    btn_stop.pack(side=tk.LEFT, padx=10)

    # Log Area
    log_label = tk.Label(root, text="Log de Atividades:")
    log_label.pack(pady=(5, 0))
    
    log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=('Courier New', 10))
    log_area.pack(padx=10, pady=10)
    
    log_message("Aplicação inicializada. Clique em EXECUTAR para começar.")

    # Garante que a automação pare ao fechar a janela
    root.protocol("WM_DELETE_WINDOW", lambda: [stop_automation(), root.destroy()])
    
    root.mainloop()

if __name__ == '__main__':
    setup_gui()