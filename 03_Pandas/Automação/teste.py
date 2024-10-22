# importar base de dados
# cadastro de produtos
# repetir até acabar a base de dados

import pyautogui 
# clicar -> pyautogui.click
# Escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey



pyautogui.PAUSE = 1
# Apertar a tecla windows 
pyautogui.press("win")

# digite o nome do programa
pyautogui.write("chrome")

# apertar enter
pyautogui.press("enter")

#digitar link, eu posso criar uma variavel
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# pressionar enter
pyautogui.press("enter")

# esperar 5 segundos
import time
time.sleep(5)

#fazer login
pyautogui.click(x=573, y=408)   

#digitar email
pyautogui.write("gustavo.teste@gmail.com")

pyautogui.press("tab")

#digitar a senha
pyautogui.write("123456")

pyautogui.click(x=670, y=566)
time.sleep(3)

# NESSA PARTE É PRA CADASTRAR OS PRODUTOS JÁ

import pandas

tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=531, y=296)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    #tipo
    tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #OBS
    obs = (tabela.loc[linha, "obs"])
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)