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

#--------------------"DISPARAGEM" DE AUTOMAÇÃO -----------------------#



#------------------ ABERTURA DO GOOGLE FORMS -------------------#

#abrir o navegador
navegador = webdriver.Chrome()

# Acessar o site
navegador.get("https://docs.google.com/forms/d/1R_ppy0-ZmkPu_U-J4hzj6Ga1IlpWVGBZndlT1ZHLn00/viewform?edit_requested=true")

#Espera a página carregar
time.sleep(1)

navegador.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
pyautogui.write('João Vítor Oliveira de Alcantara')

navegador.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
pyautogui.write('joaovitorapid@gmail.com')

pyautogui.hotkey('tab')
pyautogui.write('06')
pyautogui.write('04')
pyautogui.write('2001')

navegador.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
pyautogui.write('07578307142')

navegador.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
pyautogui.write('Passo Alto Cond.')

navegador.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
pyautogui.write('Passo Alto Cond.')

pyautogui.hotkey('tab')
pyautogui.write('20')
pyautogui.write('12')
pyautogui.write('2025')

navegador.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
time.sleep(5)
