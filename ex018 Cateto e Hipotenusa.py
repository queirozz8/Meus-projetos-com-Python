from math import hypot
print('Eu sou um algoritmo criado para fornecer a hipotenusa de um triângulo retângulo.')
co = float(input('Comprimento do cateto oposto (vertical): '))
ca = float(input('Comprimento do cateto adjacente (horizontal): '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))