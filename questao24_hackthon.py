print('Escolha uma operação')
print('1.adição')
print('2.subtração')
print('3.multiplicação')
print('4.divisão')
print('5.potenciação')

operacao = input('Digite o numero da operação desejada 1/2/3/4/5: ')

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

resultado = NOne 

if operacao == '1':
    resultado = num1 + num2
    print(f'{numero} + {num2} = {resultado:.2f}')
elif operacao == '2':
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado:.2f}')
elif operacao =='3':
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado:.2f}')
elif operacao =='4':
    if num2 != 0:
        resultado = num1 / num2
        print(f'{num1} / {num2} = {resultado:.2f}')
        print('Erro: Divisão por zero não é permitida!')
elif operacao =='5':
    resultado = num1 ** num2
    print(f'{num1} ^ {num2} = {resultado:.2f}')
else:
    print('Operação Inválida!')
