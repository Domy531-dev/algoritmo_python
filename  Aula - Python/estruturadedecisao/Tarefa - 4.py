# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se é uma letra do alfabeto
if letra.isalpha() and len(letra) == 1:
    if letra in 'aeiou':
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Entrada inválida. Digite apenas uma letra.")
