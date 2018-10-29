import random
print("Seja bem-vindo ao mundo mágico de Pylândia")
input("aperte ENTER quando estiver pronto")

r1 = input("Você gostaria de jogar com um personagem [h]omem ou [m]ulher? [h/m]: ")
if r1 == 'h':
	print("Você é Luck, um pyloto em treinamento da Frota Estelar.")
	print("Seu chefe, Obi-um, responsável pelo seu treinamento, disse que tinha algo muito importante para te contar em privado")
	r2 = input("Você vai com ele na [l]anchonete ou na [b]iblioteca? [l/b]: ")
	if r2 == 'l':
		print("Você encontra Obi-um na lanchonete.")
		print("Ele está visivelmente nervoso.")
		print("Quando te vê ele derruba sem querer um guardanapo.")
		r3 = input("Você se abaixa para pegar? [s/n]: ")
		if r3 == 's':
			print("Você se abaixa para pegar o guardanapo e percebe que tem algo escrito nele.")
			print("É um endereço. Enquanto você pensa sobre isso, você ouve alguém entrar na lanchonete.")
			print("Quando você se levanta para entregar o bilhete à Obi-um, você percebe que quem entrou foi Leila, uma famosa pyrata.")
			print("Obi-um está claramente preocupado com a presença dela e sai da lanchonete")
			r4 = input('Você deseja falar com [L]eila ou ir atrás de [O]bi-um? [L/O]: ')
			if r4 == 'L':
				print('Você vai tentar conversar com Leila, mas ela não quer conversar com um desconhecido.')
				print('Um capanga dela te dá uma surra.')
			elif r4 == 'O':
				print('Você sai correndo da lanchonete, atrás de Obi-um, mas não acha ninguém no corredor')
			else:
				print('você digitou algo errado. Comece de novo.')
		if r3 == 'n':
			print('Uma famosa pyrata chamada Leila entra na lanchonete.')
			print('Os olhos dela passam rapidamente por você e se fixam em Obi-um.')
			print("Obi-um está claramente preocupado com a presença dela e sai correndo pela porta")
			r4 = input('Você deseja falar com [L]eila ou ir atrás de [O]bi-um? [L/O]: ')
			if r4 == 'L':
				print('- Você estava sentado com Obi-um - Diz Leila - deve ser o discípulo de quem ele estava falando')
				print('Leila te entrega um envelope e pede para você entregar a Obi-um assim que encontrá-lo')
			elif r4 == 'O':
				print('Você sai correndo da lanchonete, atrás de Obi-um, mas não acha ninguém no corredor')
			else:
				print('você digitou algo errado. Comece de novo.')
	else:
		print("Essa parte do jogo não está pronta ainda")
elif r1 == 'm':
	print("Você é Leila, uma famosa pyrata.")
	print("Durante sua última aventura, você acabou se envolvendo em uma trama complexa, que envolvia a própria Frota Estela.")
	print("Ao perseguir um contrabandista até um posto além do alcance da Federação, para identificar sua fonte de Rubys, você descobriu que alguém da Frota estava ajudando ele.")
	print("Antes de descobrir quem era, você foi percebida e cercada por soldados da Federação.")
	print("Você teria morrido se não fosse pela intervenção de Obi-um, que nunca te explicou o que estava fazendo lá.")
	print("Após um longo e merecido descanso você vai atrás de respostas. Pylândia é o lugar certo para isso. Todo centro de operações da ")
	r2 = input("Você vai atrás de informações na [l]anchonete da cidade ou no [p]rédio central da Frota? [l/p]: ")
	if r2 == 'p':
		print('Ao se aproximar do prédio você percebe que essa ideia não parece tão boa.')
		print('No seu último confronto com a Frota você quese morreu. Melhor não correr o risco de ser reconhecida.')
		print('Você decide ir para a lanchonete')
	if r3 == 'l':
		pass
	else: 
		print('Seus pensamentos estão confusos, mas você se lembra do seu último confronto com a Federação.')
		print("Ir para o prédio da Federação claramente não é uma boa idéia.")
		print('Você decide ir para a lanchonete')
	print('Cheagando na lanchonete...')
else:
	print('você digitou algo errado. Comece de novo.')