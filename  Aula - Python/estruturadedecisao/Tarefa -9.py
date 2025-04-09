# Lê os três números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Exibe os números ordenados
print("Números em ordem decrescente:")
for num in numeros:
    print(num)
