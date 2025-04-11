# Inicializar os vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Ler o primeiro vetor
print("Digite 10 números para o primeiro vetor:")
for i in range(10):
    num = float(input(f"Vetor 1 - Elemento {i+1}: "))
    vetor1.append(num)

# Ler o segundo vetor
print("\nDigite 10 números para o segundo vetor:")
for i in range(10):
    num = float(input(f"Vetor 2 - Elemento {i+1}: "))
    vetor2.append(num)

# Intercalar os vetores
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Mostrar o vetor intercalado
print("\nVetor Intercalado (20 elementos):")
print(vetor3)
