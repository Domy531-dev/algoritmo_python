def imprimir_linhas(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print()  # quebra de linha após cada linha

# Exemplo de uso
n = int(input("Digite um número inteiro: "))
imprimir_linhas(n)
