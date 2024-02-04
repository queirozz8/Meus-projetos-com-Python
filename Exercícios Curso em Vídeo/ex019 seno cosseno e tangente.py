from math import radians, sin, cos, tan
print('Eu sou um algoritmo criado para calcular o seno, cosseno e tangente de um ângulo.')
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print ('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))