from PySimpleGUI import PySimpleGUI as sg

# Layout

# ---> vamos pensar em linhas e coluna
sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Nome Completo'), sg.Input(key='nome_completo', password_char='*', size=(40,2))],
    [sg.Text('Data de Nascimento'), sg.Input(key='data_nascimento', size=(10,1)), sg.Text('Idade'), sg.Input(key='idade', size=(5,1))],
    [sg.Text('Idade'), sg.Input(key='idade', password_char='*', size=(40,2))],
    [sg.Text('')],###############################################################################
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(40,2))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(40,2))],
    [sg.Checkbox('Salvar o Login? ')],
    [sg.Text('')],###############################################################################
    [sg.Button('Entrar' , size=(10, 1), pad=((150, 0), 3),button_color=('white', 'red'))],
    [sg.Listbox(values=['Opção 1', 'Opção 2', 'Opção 3'], key='chave_da_lista', size=(40,5 ))],
    [sg.FileBrowse(key='chave_do_seletor_de_arquivo')],
    [sg.FolderBrowse(key='chave_do_seletor_de_pasta')],
    [sg.CalendarButton('Selecione a data', key='chave_do_seletor_de_data')],
    [sg.Combo(values=['Opção 1', 'Opção 2', 'Opção 3'], key='chave_do_combobox', size=(20, 1))],
    [sg.Radio('Opção 1', 'opcoes', key='opcao_1'), sg.Radio('Opção 2', 'opcoes', key='opcao_2')],
    [sg.Button('Confirmar')]
    

    

    

]

# Janela 
janela = sg.Window('Tela de Login', layout)

# Ler eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Gustavo' and valores['senha'] == '123456':
            print('Bem-Vindo, meu senhor')

janela.close()