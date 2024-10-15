# Leitura de horas trabalhadas e salario minimo
horas_trabalhadas = float(input('Digite o numero de horas trabalhadas: '))
salario_minimo = float(input('Digite o salario minimo: '))

# Calcula o valor da hora trabalhada
valor_hora = salario_minimo / 2

# Calcula salario bruto
salario_bruto = horas_trabalhadas * valor_hora

# Calcula o imposto 
imposto = salario_bruto * 0.03

# Calcula o novo salario
novo_salario = salario_bruto - imposto

# Resultados
print(f'O valor do salario bruto é: {salario_bruto:.2f}')
print(f'O valor de imposto é: {imposto:.2f}')
print(f' O salario a receber é {novo_salario:.2f}')