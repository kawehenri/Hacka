# Leitura da temperatura em farenheit
farenheit = int(input('Digite a temperatura em farenheit: '))

# Formula de conversão
celsius = (5/9) * (farenheit - 32)

# Resultado
print(f'A temperatura equivalente em celsius é: {celsius:.2f} °C.')