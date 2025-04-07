# Solicita ao usuário que digite uma letra
letra = input("Digite o sexo (f ou m): ").lower()

# Verifica a letra digitada e exibe o resultado
if letra == 'f':
    print("Feminino")
elif letra == 'm':
    print("Masculino")
else:
    print("Sexo inválido")
