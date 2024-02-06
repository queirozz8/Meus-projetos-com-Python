#EN: Requests the user's name
#BR: Solicita o nome do usuário
nomecompleto = str(input('Qual é o seu nome? ')).strip()

'''EN: Tells the user's name in uppercase and lowercase letters, with all the words together, how many letters are in the user's full name, what is the first name and how many letters 
are in the user's name first name'''
'''BR: Diz o nome do usuário em letras maiúsculas, minúsculas, com todas as palavras juntas, quantas letras tem o nome completo do usuário, qual é o primeiro nome e quantas letras tem o 
primeiro nome'''
print('Em letras maiúsculas: {}'.format(nomecompleto.upper()))
print('Em letras minúsculas: {}'.format(nomecompleto.lower()))
print('Tudo junto: {}'.format(nomecompleto.replace(' ', '')))

#EN: It sepairs the user's name to speak what's the user's first name and how many letters the first name have
#BR: Separa o nome do usuário para falar qual é o primeiro nome e quantas letras tem o primeiro nome
nomes_separados = nomecompleto.split()
primeiro_nome = nomes_separados[0]
print('Quantas letras tem seu nome completo: {}'.format(len(nomecompleto) - nomecompleto.count(' ')))
print('Qual é o primeiro nome: {}'.format(primeiro_nome))
print('Quantas letras tem o primeiro nome: {}'.format(len(primeiro_nome)))
