peso_original = float(input('Digite o peso da pessoa em kg: '))
peso_ganho = peso_original*1.15
peso_perda = peso_original*0.80

print(f'O novo peso, caso a pessoa engorde 15%, será: {peso_ganho:.2f} kg')

print(f'O novo peso, caso a pessoa emagreça 20%, será: {peso_perda:.2f} kg')
