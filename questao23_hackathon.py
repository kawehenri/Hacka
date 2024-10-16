# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para determinar o grau de obesidade
def determinar_grau_obesidade(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc <= 24.9:
        return "Saudável"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Entrada de dados do usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Determinação do grau de obesidade
grau_obesidade = determinar_grau_obesidade(imc)

# Exibição dos resultados
print(f"Seu IMC é {imc:.2f} e seu grau de obesidade é: {grau_obesidade}")