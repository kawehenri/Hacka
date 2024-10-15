# Mostra o salario base
salario_base = int(input('Digite o salario base do funcionario: '))

# Define a gratificação e o percentual de imposto
gratificação = 50.00
imposto = 0.10

# Calculo de valor de imposto 
valor_imposto = salario_base * imposto

# Calculo de novo salario 
novo_salario = salario_base - valor_imposto + gratificação

# Resultados 
print(f'O valor do novo salario é de: {novo_salario:.2f}')