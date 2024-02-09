from random import choice
nome1 = str(input('Qual é o nome do primeiro aluno? '))
nome2 = str(input('Qual é o nome do segundo aluno? '))
nome3 = str(input('Qual é o nome do terceiro aluno? '))
nome4 = str(input('Qual é o nome do quarto aluno? '))
lista =[nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido foi o(a) {}'.format(escolhido))
