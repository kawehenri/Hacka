# Recebe a palavra do usuario
palavra = input('Digite uma palavra: ')

# Calcula a quantidade de letras
quantidade_letras = len(palavra)

# Verifica a quantidade de letras é par ou impar
if quantidade_letras % 2 == 0:
    print(f'A quantidade de letras na palavra {palavra} é {quantidade_letras} que é par. ')
else:
    print(f'A quantidade de letras na palavra {palavra} é {quantidade_letras} que é impar. ')