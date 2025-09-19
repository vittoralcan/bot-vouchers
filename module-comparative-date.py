import pyperclip

def converter_data_da_area_de_transferencia():
    """
    Pega uma data da área de transferência no formato DD/MM/AAAA e a converte
    para um formato como:
    dia = DD
    mes = Nome do mês AAAA
    """
    try:
        # Pega o conteúdo da área de transferência
        data_copiada = pyperclip.paste()

        # Verifica se o formato da data é o esperado
        if len(data_copiada) != 10 or data_copiada[2] != '/' or data_copiada[5] != '/':
            return "Erro: O formato da data na área de transferência não é DD/MM/AAAA."

        # Divide a string da data em dia, mês e ano
        dia_str, mes_str, ano_str = data_copiada.split('/')

        # Dicionário para converter o número do mês para o nome do mês em português
        meses = {
            "01": "Janeiro",
            "02": "Fevereiro",
            "03": "Março",
            "04": "Abril",
            "05": "Maio",
            "06": "Junho",
            "07": "Julho",
            "08": "Agosto",
            "09": "Setembro",
            "10": "Outubro",
            "11": "Novembro",
            "12": "Dezembro"
        }

        # Converte o número do mês para o nome correspondente
        nome_do_mes = meses.get(mes_str)

        if not nome_do_mes:
            return "Erro: Mês inválido na data."

        # Formata a string de saída
        data_formatada = f"dia = {dia_str}\nmes = {nome_do_mes} {ano_str}"
        
        return data_formatada

    except pyperclip.PyperclipException:
        return "Erro: Não foi possível acessar a área de transferência. Certifique-se de que a biblioteca pyperclip está instalada e que você tem permissão para acessá-la."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Imprime o resultado da conversão
print(converter_data_da_area_de_transferencia())