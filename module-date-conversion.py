import pyperclip
import datetime
import sys

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