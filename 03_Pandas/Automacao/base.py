import pyautogui 
import time

while True:
    time.sleep(5)  # Aguarda 5 segundos antes de começar, caso necessário

    # Abrir o arquivo e processar os dados
    with open(r'C:\Users\Gustavo Caris\Desktop\GUSTAVO\Data_Science\03_Pandas\Automacao\customers.txt', 'r') as arquivo:
        for linha in arquivo:
            NomeCliente = linha.split(',')[0]
            Email = linha.split(',')[1]
            Contato = linha.split(',')[2]

            # Primeiro clique, que deve ser feito para cada cliente lido
            pyautogui.click(1185,312, duration=1)
            
            # Segundo clique (conforme seu código)
            pyautogui.click(516,332, duration=1)
            pyautogui.write(NomeCliente)
            # Interagir com a interface, preenchendo os campos
            pyautogui.click(518,413, duration=1)
            pyautogui.write(Email)
            pyautogui.click(512,501, duration=1)
            pyautogui.write(Contato)
            pyautogui.click(766,577, duration=1)
            

            # Finalizar ação
            pyautogui.click(776, 582, duration=1)

            # Recarregar página ou alguma ação extra
            pyautogui.moveTo(772,490)
            time.sleep(7)
            pyautogui.click(772,490)

    
            # scroll pra baixo
            pyautogui.scroll(-500)
            time.sleep(5)

    # Aqui o loop volta a ler o arquivo novamente desde o início
