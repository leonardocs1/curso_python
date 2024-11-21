nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

# f-strings
linha1 = f'{nome} tem {altura:.2f} de altura,'
linha2 = f'pesa {peso} quilos e seu IMC é '
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)