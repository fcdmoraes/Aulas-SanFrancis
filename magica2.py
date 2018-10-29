print("Vamos fazer uma mágica?")
print('Pense em um número entre 1 e 10')
input("\nAperte 'Enter' para começar\n")

r1 = input("Seu número tem a letra 'o' no nome? [sim/não] ")
r2 = input("Seu número é múltiplo de 2? [sim/não] ")
r3 = input("O nome do seu número tem 4 letras? [sim/não] ")

if (r1,r2,r3) == ('sim','sim','sim'):
	r4 = input('O dobro do seu número é maior do que 10? [sim/não] ')
	if r4 == 'sim':
		print('seu número é oito')
	elif r4 == 'não':
		print('seu número é dois')
	else:
		print('ops, parece que você respondeu algo errado')
elif (r1,r2,r3) == ('sim','sim','não'):
	print('seu número é quatro')
elif (r1,r2,r3) == ('sim','não','sim'):
	print('seu número é nove')
elif (r1,r2,r3) == ('sim','não','não'):
	print('seu número é cinco')
elif (r1,r2,r3) == ('não','sim','sim'):
	print('seu número é seis')
elif (r1,r2,r3) == ('não','sim','não'):
	print('seu número é dez')
elif (r1,r2,r3) == ('não','não','sim'):
	print('seu número é um')
elif (r1,r2,r3) == ('não','não','não'):
	r4 = input('O dobro do seu número é maior do que 10? [sim/não] ')
	if r4 == 'sim':
		print('seu número é sete')
	elif r4 == 'não':
		print('seu número é três')
	else:
		print('ops, parece que você respondeu algo errado')
else:
	print('ops, parece que você respondeu algo errado')