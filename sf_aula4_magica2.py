print("escolha um número de 1 a 10")
input("aperte ENTER quando estiver pronto")

r1 = input("seu número tem a letra 'o' no nome? [s/n]: ")
if r1 == 's':
	r2 = input("seu número é múltiplo de 2? [s/n]: ")
	if r2 == 's':
		r3 = input("o número de letras no seu número é igual a 4? [s/n]: ")
		if r3 == 's':
			r4 = input('O dobro do seu número é maior do que 10? [s/n]: ')
			if r4 == 's':
				print('seu número é 8')
			elif r4 == 'n':
				print('seu número é 2')
			else:
				print('você digitou algo errado. Comece de novo.')
		else:
			print('seu número é 4')
	else:
		r3 = input("o número de letras no seu número é igual a 4? [s/n]: ")
		if r3 == 's':
			print('seu número é 9')
		else:
			print('seu número é 5')
else:
	r2 = input("seu número é múltiplo de 2? [s/n]: ")
	if r2 == 's':
		r3 = input("o número de letras no seu número é igual a 4? [s/n]: ")
		if r3 == 's':
			print('seu número é 6')
		else:
			print('seu número é 10')
	else:
		r3 = input("o número de letras no seu número é igual a 4? [s/n]: ")
		if r3 == 's':
			r4 = input('O dobro do seu número é maior do que 10? [s/n]: ')
			if r4 == 's':
				print('seu número é 3')
			else:
				print('seu número é 7')
		else:
			print('seu número é 1')
