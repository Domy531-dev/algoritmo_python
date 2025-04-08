# Leitura das duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Exibição do resultado
print(f"Média: {media:.2f}")

# Verificação da aprovação
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
