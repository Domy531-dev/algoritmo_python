# Validação de Nome
while True:
    nome = input("Digite o nome (mais de 3 caracteres): ")
    if len(nome) > 3:
        break
    print("Nome inválido. Deve conter mais de 3 caracteres.")

# Validação de Idade
while True:
    try:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. Deve estar entre 0 e 150.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Validação de Salário
while True:
    try:
        salario = float(input("Digite o salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário inválido. Deve ser maior que zero.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Validação de Sexo
while True:
    sexo = input("Digite o sexo ('f' para feminino ou 'm' para masculino): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo inválido. Use 'f' ou 'm'.")

# Validação de Estado Civil
while True:
    estado_civil = input("Digite o estado civil ('s' - solteiro, 'c' - casado, 'v' - viúvo, 'd' - divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    print("Estado civil inválido. Use 's', 'c', 'v' ou 'd'.")

# Exibindo as informações validadas
print("\nInformações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {estado_civil.upper()}")
