from selenium import webdriver
import pyautogui
import time

# - Section 1 - Abrir o navegador 

navegador=webdriver.Chrome()

navegador.get('https://docs.google.com/spreadsheets/d/1ylJBsGHpnk0qSENfGcpDobomFwW0SFmBQypN_VwuiN8/edit?resourcekey=&gid=619559408#gid=619559408')
time.sleep(4)

navegador.quit()
