# Mostra o salario atual e o percentual de aumento
salario = int(input('Digite o salario atual: '))
percentual_aumento = int(input('Digite o percentual de aumento: '))

# Calculo de percentual de aumento
aumento = salario * (percentual_aumento / 100)

# Calcula o novo salario
novo_salario = salario + aumento

# Resultados
print(f' O valor de aumento é: {aumento:.2f}')
print(f'O novo salario é: {novo_salario:.2f}')