from random import randint
from time import sleep

'''OBS: Maybe for some peaple this game will end up being very difficult to get right, I ask you to try
        more times, one moment you get it right, the program it's working normally.'''
'''OBS: Talvez para algumas pessoas esse jogo acabe sendo muito difícil de se acertar, peço para que tentem
      mais vezes, uma hora você acerta, o programa não está com bugs. '''
      
print('''OBS: Talvez para algumas pessoas esse jogo acabe sendo muito difícil de se acertar, peço para que tentem
      mais vezes, uma hora você acerta, o programa não está com bugs. ''')
print('-=-' * 26)
print('Vou pensar em um número entre 1 até 5, tente adivinhar que número eu pensei! ')
print('-=-' * 26)
# The computer draws the numbers of the list (1 to 5)
# Faz o computador sortear os números da lista (1 até 5)
computador = randint(1, 5)
# Player try to guess the number
# Jogador tenta adivinhar o número
resposta = int(input('Qual número eu pensei? '))
# The computer pretend to be "processing", for give to the user some imersion
# O computador finge estar "processando", para dar uma imersão para o usuário
print('PROCESSANDO...')
sleep(0.5)
# If the number that the user spoke is the same as the number that the computer thought:
# Se a o número que o usuário falou foi igual ao número que o computador pensou: 
if resposta == computador:
    print(f'Parabéns, você acertou! Eu estava pensando no número {computador}!')
else: # If isn't:    # Se não foi:
    print(f'Que pena, você errou. Eu pensei no número {computador} e não no número {resposta}.')
