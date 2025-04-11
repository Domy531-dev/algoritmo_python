# Criar uma lista vazia
numeros = []

# Ler 10 números reais do usuário
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

# Mostrar os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(numeros):
    print(numero)
