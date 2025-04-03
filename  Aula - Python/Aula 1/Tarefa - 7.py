def calcular_area_quadrado(lado):
    return lado ** 2

# Exemplo de uso
lado = float(input("Digite o lado do quadrado: "))
area = calcular_area_quadrado(lado)
dobro_area = area * 2
print(f"A área do quadrado é {area:.2f} e o dobro da área é {dobro_area:.2f}.")