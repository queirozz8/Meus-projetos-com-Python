'''Você pode fazer desse jeito:
from math import trunc
print('Esse é um algoritmo que diz a parte inteira de um número real')
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

mas eu vou fazer de outro jeito pois possui menos linhas de código:  '''
print('Esse é um algoritmo que diz a parte inteira de um número real')
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
