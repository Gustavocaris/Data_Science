import pyautogui 
import time


time.sleep(5)

pyautogui.click(1186,309, duration=2)

pyautogui.click(584,331, duration=2)

with open('CustomersTest.txt', 'r') as arquivo:
    for linha in arquivo:
        nome = linha.split(',')[0]
        email = linha.split(',')[1]
        contato = linha.split(',')[2]



# function mouse

#pyautogui.click(x=684, y=557)
