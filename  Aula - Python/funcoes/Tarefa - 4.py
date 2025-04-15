def verifica_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Exemplo de uso:
valor = float(input("Digite um número: "))
resultado = verifica_sinal(valor)
print("Resultado:", resultado)
