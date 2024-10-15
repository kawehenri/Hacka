# Exibe as opções de operação
print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potenciação")

# Lê a operação escolhida pelo usuário
operacao = input("Digite o número da operação desejada (1/2/3/4/5): ")

# Lê os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Inicializa a variável resultado
resultado = None

# Realiza a operação escolhida
if operacao == '1':
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado:.2f}")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado:.2f}")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado:.2f}")
elif operacao == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida!")
elif operacao == '5':
    resultado = numero1 ** numero2
    print(f"{numero1} ^ {numero2} = {resultado:.2f}")
else:
    print("Operação inválida!")