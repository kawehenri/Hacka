# Leitura de medida de pés
pés = int(input('Digite a medida em pés: '))

# Conversão para polegadas
polegadas = pés * 12

# Converte para jardas
jardas = pés / 3

# Converte para milhas
milhas = jardas / 1760

# Resultados
print(f'A medida em polegadas é: {polegadas:.2f} polegadas.')
print(f'A medida em jardas é: {jardas:.2f} jardas. ')
print(f'A medida em milhas é: {milhas:.2f} milhas. ')
