def fahrenheit_para_celsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)

# Exemplo de uso
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"A temperatura em graus Celsius é {celsius:.2f}°C.")
