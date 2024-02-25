# OPERADORES LOGICOS: and, or , not
# dar uma olhada na tabela verdade


# ---------AND--------------Para participar de um evento tem que ser maior de 18 e ter mais de 1.70
# idade = 15
# altura = 1.75

# resultado = (idade >= 18) and (altura >=1.70)
# msg = 'Pode participar do evento? ' + str(resultado)

# print(msg)



# ---------OR---------------programa de disparo de alarme com a porta aberta
# porta = 'f'
# janela = 'f'

# alarme = (porta == 'a') or (janela == 'a')
# msg = 'Alarme disparado?  ' + str(alarme)

# print(msg)

#--------NOT-----------para fazer uma compra preciso ter dinheiro

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro  # recebeu um pix e 'inverte o estado logico'

msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)