import pyautogui 
import time


time.sleep(5)

pyautogui.click(1186,309, duration=2)

pyautogui.click(584,331, duration=2)

with open(r'C:\Users\Gustavo Caris\Desktop\GUSTAVO\Data_Science\03_Pandas\Automacao\customers.txt', 'r') as arquivo:

    for linha in arquivo:
        NomeCliente = linha.split(',')[0]
        Email = linha.split(',')[1]
        Contato = linha.split(',')[2]
        pyautogui.click(584,331, duration=2)
        pyautogui.write(NomeCliente)
        pyautogui.click(608,421, duration=2)
        pyautogui.write(Email)
        pyautogui.click(571,499, duration=2)
        pyautogui.write(Contato)

        #finish
        pyautogui.click(776,582, duration=2)
        




# function mouse

#pyautogui.click(x=684, y=557)
