from random import randint # randint é o 'dado', a pontuação dos jogadores vai se basear nele
from time import sleep # sleep é só para ter uma UX mais legal
from operator import itemgetter

print('-='*40)
print(f'{'JOGO DE DADOS':^70}')
print(f'{'5 jogadores irão girar um dado de 6 lados e verão suas pontuações.':^70}')
print(f'{'Após isso, terá o ranking.':^70}')
print('-='*40)

# Definimos os jogadores, cada um vai escolher um número de 1 até 6 com o randint:
jogo = {
    'Jogador_1': randint(1,6),
    'Jogador_2': randint(1,6),
    'Jogador_3': randint(1,6),
    'Jogador_4': randint(1,6),
    'Jogador_5': randint(1,6)}
# ranking é uma lista que vamos utilizar para ordenar a pontuação dos jogadores para mostrar no final:
ranking = []

# Para cada chave (k de key), valor (v de value) nos itens de jogo:
for k, v in jogo.items():
    # k é o jogador atual, v é o valor que ele está:
    print(f'{k} girou o dado e ficou com {v}.')
    sleep(0.5)
print('-='*40)

print(f'{'=== RANKING DOS JOGADORES ===':^70}')
# ranking recebe o dicionário 'jogo' ordenado com o sorted, porém precisamos especificar o que queremos que o sorted organize. É aí que vem o itemgetter. 
# Estamos passando como key que queremos que sorted ordene todos os itens de índice 1 (Graças ao itemgetter) de todas as chaves. 
# Como o sorted ordena do menor para o maior, e queremos fazer um top, invertemos com o reverse=True:
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# ranking é uma lista, então usamos o enumerate. Para cada valor (v) dentro de ranking, com o índice de cada item sendo armazenado por i:
for i, v in enumerate(ranking):
    # Mostre o índice do item atual (Como começa com 0, então colocamos +1 para mostrar de forma mais 'humanizada' para o usuário),
    # mostre v na posição 0 (que seria o nome do jogador atual), depois mostre os pontos dele com v[1]:
    print(f'{f'{i+1}° lugar: {v[0]}, com {v[1]} ponto(s).':^70}')
    sleep(0.5)
print()