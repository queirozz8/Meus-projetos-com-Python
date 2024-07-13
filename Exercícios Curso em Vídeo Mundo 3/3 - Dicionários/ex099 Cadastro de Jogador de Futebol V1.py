print('-='*30)
print(f'{'SOFTWARE DE APROVEITAMENTO DE JOGADOR DE FUTEBOL':^60}')
print('-='*30)

# jogador é um dicionário onde vai armazenar o nome dele, os gols que ele fez em cada partida e total de gols que ele fez:
jogador = {}
# gols_partidas é onde vai ser armazenado cada gol de cada partida:
gols_partidas = []
jogador['Nome'] = input('Digite o nome do jogador: ').lstrip().rstrip()
tot_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
# Contador que vai de 0 até o total de partidas:
for c in range(tot_partidas):
    # c começa com 0, então colocamos +1 para mostrar de forma mais 'Humanizada' para o usuário:
    gols_partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
# Gols recebe uma cópia de todos os valores de gols_partidas:
jogador['Gols'] = gols_partidas[:]
# E Total recebe a soma de todos os elementos de gols_partidas:
jogador['Total'] = sum(gols_partidas)

print('-='*30)
print(f'{'RESULTADO DOS JOGOS':^60}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {tot_partidas} jogos de Futebol.')
# Para cada valor dentro de gols_partidas, sendo que i é o índice de cada partida:
for i, v in enumerate(gols_partidas):
    print(f' ->  NA PARTIDA {i+1}, {jogador["Nome"]} FEZ {v} GOL(S).')
print('-='*30)
print(f'Sendo assim, um TOTAL de {jogador["Total"]} GOL(S). \n')