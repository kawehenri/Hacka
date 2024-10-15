# Função para calcular a data de devolução
def calcular_devolucao(dia, mes, ano, tipo_usuario):
    if tipo_usuario.lower() == 'professor':
        dias_adicionados = 20
    elif tipo_usuario.lower() == 'aluno':
        dias_adicionados = 15
    else:
        return None

    # Adiciona os dias ao dia atual
    dia += dias_adicionados

    # Ajusta o mês e o ano se necessário
    if mes == 2:  # Fevereiro
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  # Ano bissexto
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    elif mes in [4, 6, 9, 11]:  # Meses com 30 dias
        dias_no_mes = 30
    else:  # Meses com 31 dias
        dias_no_mes = 31

    if dia > dias_no_mes:
        dia -= dias_no_mes
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1

    return dia, mes, ano

# Lê o nome do livro
nome_livro = input("Digite o nome do livro: ")

# Lê o tipo de usuário
tipo_usuario = input("Digite o tipo de usuário (professor ou aluno): ")

# Lê a data de empréstimo
data_emprestimo_str = input("Digite a data do empréstimo (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_emprestimo_str.split('/'))

# Calcula a data de devolução
data_devolucao = calcular_devolucao(dia, mes, ano, tipo_usuario)

# Verifica se o tipo de usuário é válido
if data_devolucao is None:
    print("Tipo de usuário inválido! Por favor, insira 'professor' ou 'aluno'.")
else:
    dia_devolucao, mes_devolucao, ano_devolucao = data_devolucao
    # Exibe o recibo
    print("\nRecibo:")
    print(f"Nome do livro: {nome_livro}")
    print(f"Tipo de usuário: {tipo_usuario.capitalize()}")
    print(f"Data do empréstimo: {dia:02}/{mes:02}/{ano}")
    print(f"Data da devolução: {dia_devolucao:02}/{mes_devolucao:02}/{ano_devolucao}")