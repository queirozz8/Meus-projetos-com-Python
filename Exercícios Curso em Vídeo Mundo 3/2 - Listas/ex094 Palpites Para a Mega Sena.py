from random import randint
from time import sleep
print('-='*30)
print(f'{'MEGA SENA':^60}')
print(f'{'Cada jogo custa R$5,00.':^60}')
print('-='*30)

# lista é uma lista temporária onde os jogos vão ser armazenados, ordenados e depois passados para jogos:
lista = []
# jogos é a lista principal que vamos manipular. Nela, todos os jogos vão ficar armazenados:
jogos = []
# quant é a quantidade de jogos que o usuário quer jogar:
quant = int(input('Digite quantos jogos deseja sortear: '))
# Calculamos o preço de todos os jogos:
preco = 5 * quant
# tot é o contador que vai definir em qual jogo estamos atualmente.
tot = 1
# Vamos supor que o usuário quis sortear 5 jogos. Quando jogos estiver com 3 elementos e tot estiver com 4, tot ainda vai ser menor do que quant, então lista vai receber mais um jogo, passar para jogos e
# jogos vai ter 4 elementos. Depois, tot fica com 5 (por isso o "menor ou IGUAL", pois agora tot tem a mesma quantidade do que quant, e queremos que o loop não pare, queremos que ele continue para que jogos
# receba mais um jogo), após isso jogos fica com 5 e tot fica com 6. Por isso colocamos "menor ou igual", não só "menor":
while tot <= quant:
    cont = 0
    # Esse loop cria um novo jogo da Mega sena, manda ele para lista, lista ordena os números, manda o jogo para jogos e depois se apaga: 
    while True:
        num = randint(1, 60)
        # Não queremos números repetidos, então só vamos adicionar o número à lista caso ele não esteja nela:
        if num not in lista:
            lista.append(num)
            cont += 1
        # Quando cont for igual à 6, ou seja, já pegamos 6 números e colocamos dentro da lista:
        if cont == 6:
            break
    # Ordena a lista dos números:
    lista.sort()
    # Manda para jogos, que é nossa lista principal:
    jogos.append(lista[:])
    # Se apaga, para que outro jogo venha e o ciclo continue:
    lista.clear()
    tot += 1

print(f'SORTEANDO {quant} NÚMEROS...')
# Para cada jogo na lista jogos, sendo que ind_jogo é o índice do jogo atual:
for ind_jogo, jogo in enumerate(jogos):
    print(f'Jogo {ind_jogo+1}: {jogo}')
    sleep(0.5)
print('-'*30)
print(f'Isto custará R${float(preco)}.')
print('-=-=-= BOA SORTE! -=-=-=')