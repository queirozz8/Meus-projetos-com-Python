import random
print('Eu sou um algoritmo criado para embaralhar uma ordem de alunos para apresentar um trabalho escolar.')
n1 = str(input('Qual é o nome do primeiro aluno? '))
n2 = str(input('Qual é o nome do segundo aluno? '))
n3 = str(input('Qual é o nome do terceiro aluno? '))
n4 = str(input('Qual é o nome do quarto aluno? '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação do trabalho será: {}'.format(lista))
