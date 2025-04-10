# Loop para garantir que a nota esteja entre 0 e 10
while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print("Nota ok!")
            break  # Sai do loop se a nota for válida
        else:
            print("Nota inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número.")
