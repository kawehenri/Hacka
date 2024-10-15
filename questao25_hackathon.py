# Receber a letra
letra = input('Digite uma letra: ').lower()

# Verifica se é vogal ou consoante
if len(letra) == 1:
    if letra >= 'a' and letra <= 'z':
        if letra in 'aeiou':
            print(f'A letra {letra} é uma vogal. ')
        else:
            print(f'A letra {letra} é uma consoante. ')