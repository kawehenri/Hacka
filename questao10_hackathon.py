# Leitura de numero positivo > 0
numero = float(input('Digite um numero positivo maior que zero: '))

# Verifica se o numero é valido
if numero > 0:
    # Calculo de numero ao quadrado
    quadrado = numero ** 2
    # Calculo de numero ao cubo
    cubo = numero ** 3
    # Calculo de raiz quadrada
    raiz_quadrada = numero ** 0.5
    # Calculo de raiz cubica
    raiz_cubica = numero ** (1/3)
    # Resultados
    print(f'O numero {numero} ao quadrado é: {quadrado:.2f}')
    print(f'O numero {numero} ao cubo é: {cubo:.2f}')
    print(f' A raiz quadrada do numero {numero} é: {raiz_quadrada:.2f}')
    print(f' A raiz cubica do numero {numero} é: {cubo:.2f}')

else:
    print('O numero deve ser positivo e maior que zero. ')