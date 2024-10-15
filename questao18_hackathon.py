# Leitura da viagem em km
percurso = float(input('Digite o percurso da viagem: '))

# Recebe o tipo de carro
print('Tipos de carro: A, B e C. ')
tipo_carro = input('Digite o tipo de carro: ').upper()

# Recebe o preço do combustivel
preço_litro = float(input('Digite o preço do litro do combustivel: '))

# Verificação de carro
if tipo_carro == 'A':
    autonomia = 16
elif tipo_carro == 'B':
    autonomia = 12
elif tipo_carro == 'C':
    autonomia = 8
else:
    print('Tipo de carro invalido! ')
    exit()

# Calculo de consumo
litros_consumidos = percurso / autonomia

# Calculo de valor estimado da viagem
valor_viagem = litros_consumidos * preço_litro

# Resultados
print(f'Litros de combustivel necessario: {litros_consumidos:.2f} L.')
print(f'O valor estimado da viagem: {valor_viagem:.2f}')