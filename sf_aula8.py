##lista = [1,3,7,4,3,7,8]
##
##print(lista[0])
##print(len(lista))
##
##lista.append(0)
##print(lista)
##
##lista.insert(1,2)
##print(lista)
##
####lista.remove(3)
####print(lista)
##
##while 3 in lista:
##    lista.remove(3)
##
##print(lista)
##
##x=lista.pop(2)
##print(lista)
##print(x)

baralho = []

carta = 1
while carta <= 10:
    baralho.append(carta)
    carta = carta + 1
while len(baralho)<13:
    baralho.append(10)

baralho = baralho * 4
print(baralho)

import random

pontos = 0
while input("para comprar uma carta, digite 's': ") == 's':
    r = random.randint(0,len(baralho)-1)
    carta = baralho.pop(r)
    print("carta sorteada: ",carta)
    pontos = pontos + carta
    print("total de pontos: ",pontos)
    if pontos >= 21:
        break

pontos_comp = 0
r = random.randint(0,len(baralho)-1)
carta = baralho.pop(r)
pontos_comp = pontos_comp + carta












