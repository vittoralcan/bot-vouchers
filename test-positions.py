def converter_data_da_area_de_transferencia():
    """
    Pega uma data da área de transferência no formato DD/MM/AAAA e a converte
    para um dicionário com 'dia', 'mes' e 'ano'.
    """
    try:
        data_copiada = pyperclip.paste()
        if len(data_copiada) != 10 or data_copiada[2] != '/' or data_copiada[5] != '/':
            print("Erro: O formato da data na área de transferência não é DD/MM/AAAA.")
            return None

        dia_str, mes_str, ano_str = data_copiada.split('/')

        meses = {
            "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
            "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
            "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
        }

        nome_do_mes = meses.get(mes_str)
        if not nome_do_mes:
            print("Erro: Mês inválido na data.")
            return None

        return {
            "dia": dia_str,
            "mes": nome_do_mes,
            "ano": ano_str
        }

    except pyperclip.PyperclipException:
        print("Erro: Não foi possível acessar a área de transferência.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro na conversão da data: {e}")
        return None

def navegar_para_mes_correto(driver, wait, data_alvo):
    """
    Navega pelos meses do calendário até encontrar o mês e ano corretos.
    """
    mes_alvo_completo = f"{data_alvo['mes']} {data_alvo['ano']}".upper()
    print(f"Mês e ano alvo: {mes_alvo_completo}")

    tentativas = 0
    max_tentativas = 24  # Limite para evitar loop infinito

    while True:
        if tentativas >= max_tentativas:
            print("Erro: Não foi possível encontrar o mês alvo após 24 tentativas. Verifique a data ou o calendário.")
            return False

        # Extrai o mês e ano do calendário visível
        try:
            mes_ano_calendario = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-switch'))).text
            print(f"Mês e ano do calendário atual: {mes_ano_calendario.upper()}")
        except:
            print("Erro ao tentar ler o cabeçalho do calendário. O calendário pode ter fechado.")
            return False

        # Compara o mês da data copiada com o mês do calendário
        if mes_ano_calendario.upper() == mes_alvo_completo:
            print("Mês correto encontrado!")
            return True
        else:
            print("Mês incorreto. Avançando para o próximo mês...")
            # Clica no botão de "avançar" (seta para a direita)
            driver.find_element(By.CLASS_NAME, 'next').click()
            time.sleep(1) # Pequena pausa para a transição
            tentativas += 1

def selecionar_data_no_calendario():
    """
    Função principal que automatiza a seleção da data no calendário.
    """
    # 1. Converte a data da área de transferência
    data_alvo = converter_data_da_area_de_transferencia()
    if not data_alvo:
        return

    # 2. Configura o driver do Selenium
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Acessa a URL e faz o login
        url = "https://www.unisystemtec.com.br/portal_socio/index.php?class=LoginForm"
        driver.get(url)

        wait = WebDriverWait(driver, 20)
        
        # Lógica de Login (ajustada para waits)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/div/div[2]/input'))).click()
        driver.find_element(By.NAME, 'login_id').send_keys('6696')
        driver.find_element(By.NAME, 'login_password').send_keys('32901548000107')
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button'))).click()

        # Navega para a página com o calendário (ajustado para waits)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/a'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[1]/aside/div[2]/div/ul/li[4]/ul/li[1]/a'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div[1]/div/div/div/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/input'))).click()

        # Espera o calendário aparecer
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-inline')))
        
        # 3. Chama a nova função para encontrar o mês correto
        if not navegar_para_mes_correto(driver, wait, data_alvo):
            return

        # 4. Encontra e clica no dia correspondente (agora que o mês está correto)
        xpath_dia = f"//td[@class='day' and text()='{int(data_alvo['dia'])}']"
        elemento_dia = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_dia)))
        elemento_dia.click()
        print(f"Dia {data_alvo['dia']} selecionado com sucesso!")

        time.sleep(3) # Pausa para ver a seleção antes de fechar

    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")

    finally:
        # Fecha o navegador
        driver.quit()

# Executa a função principal
selecionar_data_no_calendario()