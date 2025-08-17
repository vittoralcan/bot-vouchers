import pyautogui
import time

print("Movimente o mouse para a posição desejada. A posição será registrada em 5 segundos.")
time.sleep(5)

x, y = pyautogui.position()
print(f"A posição atual do mouse é: X={x}, Y={y}")