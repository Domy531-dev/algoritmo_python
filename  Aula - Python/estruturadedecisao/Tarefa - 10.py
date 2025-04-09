# Solicita o turno do usuário
turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ").upper()

# Verifica o turno e imprime a mensagem correspondente
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
