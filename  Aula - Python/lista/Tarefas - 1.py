# Criar uma lista vazia
numeros = []

# Ler 5 números inteiros do usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Mostrar os números digitados
print("Os números digitados foram:")
for numero in numeros:
    print(numero)
