import os

 # Pede ao usuário o caminho de um arquivo de texto, lê seu conteúdo e o imprime no terminal.
def ler_arquivo_de_texto(): 


    # Caminho do arquivo de texto
    caminho_do_arquivo = r"D:\\Projetos\\Tesseratto\\PROJETO - SEICON-DF\\automations\\bot-vouchers\\last_time.txt"

    
    # Adicionamos uma verificação simples para garantir que o caminho existe
    if not os.path.exists(caminho_do_arquivo):
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return

    print("\n--- Conteúdo do arquivo ---")
    try:
        # Usamos 'with' para garantir que o arquivo seja fechado automaticamente
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

if __name__ == "__main__":
    ler_arquivo_de_texto()