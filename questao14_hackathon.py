# Leitura de base e altura do retangulo
base = float(input('Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))

# Calculo de area
area = base * altura

# Calculo de perimetro
perimetro = 2 * (base + altura)

# Calculo de diagonal
diagonal = (base**2 + altura**2) ** 0.5

# Resultados
print(f'O valor da area é: {area:.2f} ')
print(f'O valor do perimetro é: {perimetro:.2f}')
print(f'O valor da diagonal é: {diagonal:.2f}')