from selenium import webdriver #lautomação do navegador
import pyautogui #automação do teclado e mouse
import time #tempo de espera
import pyperclip #manipulação da área de transferência
import os #interação com o sistema operacional

# - Section 1 - Abrir o navegador 

navegador=webdriver.Chrome()

navegador.get('https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408')
time.sleep(4)

pyautogui.press("down")
pyautogui.hotkey('ctrl','c')

def ler_e_imprimir_clipboard(): 
#Lê o conteúdo da área de transferência e o imprime no terminal.
    try:
        conteudo = pyperclip.paste()
        print("Conteúdo da área de transferência:")
        print("---")
        print(conteudo)
    except pyperclip.PyperclipException as e:
        print(f"Não foi possível acessar a área de transferência. Erro: {e}")

if __name__ == "__main__":
    ler_e_imprimir_clipboard()
time.sleep(2) #próximo passo






time.sleep(4)

navegador.quit()
