valor1 = float(input('digite um número: '))
operador = input('digite a operação: ')
valor2 = float(input('digite um número: '))
if operador == '+':
	print('Resultado é igual a {} + {} = {}'.format(valor1, valor2, valor1+valor2))
elif operador== '-':
	print('Resultado é igual a {} - {} = {}'.format(valor1, valor2, valor1-valor2))
elif operador== '*':
	print('Resultado é igual a {} * {} = {}'.format(valor1, valor2, valor1*valor2))
elif operador== '/':
	print('Resultado é igual a {} / {} = {}'.format(valor1, valor2,valor1/valor2))
else:
	print('operação invalida')