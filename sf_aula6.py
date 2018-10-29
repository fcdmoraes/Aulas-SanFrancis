##i = 0
####soma = 0
##produto = 1
##while i < 6:
##    i = i + 1
####    print(i)
####    soma = soma + i
##    produto = produto * i
####print(soma)
##print(produto)
import random
"""versão 1"""
num = random.randint(1,10)
chute = int(input("Chute um número entre 1 e 10"))
while chute != num:
	if chute > num:
		print("Chute mais baixo")
	else:
		print("Chute mais alto")
	chute = int(input("Chute um número entre 1 e 10"))
print("Você acertou!")

import time
"""versão 2"""
num = random.randint(1,10)
chute = 0
while True:
	chute = int(input("Chute um número entre 1 e 10"))
	if chute > num:
		print("Chute mais baixo")
	elif chute < num:
		print("Chute mais alto")
	else:
		print("Você acertou!")
		time.sleep(5)
		break















