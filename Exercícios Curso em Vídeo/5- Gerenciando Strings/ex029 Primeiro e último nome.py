nome = str(input('Qual é o seu nome completo? ')).strip()

#EN: It sepairs the user's full name
#BR: Separa o nome do usuário
partes_do_nome = nome.split()
print('Muito prazer em te conhecer!')

#EN: It takes the user's first and last name, for the last name, you'll need the functionality len -1, to take the last element of the list
#BR: Pega o primeiro nome e pega o último nome do usuáro, para pegar o último, você precisa usar a funcionalidade len -1, para pegar o último elemento da lista
print('O seu primeiro nome é {} e o seu último nome é {}'.format(partes_do_nome[0], partes_do_nome[len(partes_do_nome)-1]))
