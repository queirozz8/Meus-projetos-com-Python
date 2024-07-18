from random import randint
from time import sleep

# numeros é a lista com todos os números que o randint gerar:
numeros = []
# pares é a lista com todos os números pares que o sum vai somar:
pares = []
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    # Para cada número de 0 até 5:
    for num in range(5):
        # Adicione um número aleatório entre 0 e 20 na lista numeros:
        numeros.append(randint(0, 20))
        # Mostre o número adicionado, com o flush pois queremos mostrar com um intervalo de tempo:
        print(numeros[num], end=', ',flush=True)
        sleep(0.5)
    print('PRONTO!')


def soma_par():
    print(f'Somando os valores pares de ', end='')
    # Para cada numero na lista numeros:
    for num in numeros:
        # Mostre o número atual, com uma vírgula e espaço no final e com o flush, pois queremos mostrar com um intervalo de tempo:
        print(num, end=', ', flush=True)
        sleep(0.5)
        # Se o número atual for par:
        if num % 2 == 0:
            # Adiciona esse número na lista pares, para ele ser somado depois:
            pares.append(num)
    print(f'que são os números... ', end='')
    # Para cada número na lista pares:
    for num in pares:
        # Mostra o número, com uma vírgula e espaço no final e com o flush, pois queremos mostrar com um intervalo de tempo:
        print(num, end=', ', flush=True)
        sleep(0.5)
    # Somamos a lista pares com o sum:
    print(f'temos {sum(pares)}.')


# Programa Principal
sorteia()
soma_par()