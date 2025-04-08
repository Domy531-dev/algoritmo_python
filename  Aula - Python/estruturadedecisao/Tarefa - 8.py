# Lê os preços dos três produtos
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

# Verifica qual é o mais barato
if preco1 <= preco2 and preco1 <= preco3:
    mais_barato = preco1
    produto = "primeiro"
elif preco2 <= preco1 and preco2 <= preco3:
    mais_barato = preco2
    produto = "segundo"
else:
    mais_barato = preco3
    produto = "terceiro"

# Exibe o resultado
print(f"Você deve comprar o {produto} produto, que custa R${mais_barato:.2f}")
