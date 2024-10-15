# Leitura de valores
valor_inicial = float(input('Digite o valor inicial da prestação: '))
taxa_juros = float(input('Digite a taxa de juros ao dia: '))
dias_atraso = float(input('Digite o numero de dias de atraso: '))

# Conversão de juros em percentual para decimal
juros_decimal = taxa_juros / 100

# Calcula o valor de juros
juros = valor_inicial * juros_decimal + dias_atraso

# Calcula o valor total da prestação 
valor_total = valor_inicial + juros

# Resultados
print(f'O valor de juros em atraso é: {juros:.2f}')
print(f'O valor total da prestação em atraso é: {valor_total:.2f}')
