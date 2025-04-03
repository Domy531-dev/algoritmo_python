def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Exemplo de uso
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}°F.")
