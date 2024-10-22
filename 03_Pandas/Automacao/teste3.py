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
            pyautogui.click(1186, 309, duration=2)
            
            # Segundo clique (conforme seu código)
            pyautogui.click(584, 331, duration=2)

            # Interagir com a interface, preenchendo os campos
            pyautogui.click(584, 331, duration=1)
            pyautogui.write(NomeCliente)
            pyautogui.click(520, 418, duration=1)
            pyautogui.write(Email)
            pyautogui.click(571, 499, duration=1)
            pyautogui.write(Contato)

            # Finalizar ação
            pyautogui.click(776, 582, duration=1)

            # Recarregar página ou alguma ação extra
            pyautogui.click(572, 494, duration=8)

    # Aqui o loop volta a ler o arquivo novamente desde o início
