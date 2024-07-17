print('-'*30)
print(f'{'FORMAÇÃO DE TIME DE FUTEBOL':^30}')


# jogador é um dicionário temporário que vai armazenar o jogador atual:
jogador = {}
# time vai ser a lista onde todos os dicionários de jogadores vão ficar:
time = []
# gols vai ser a lista temporária que vai armazenar todos os gols do jogador atual: 
gols = []

while True:
    print('-'*30)
    jogador['Nome'] = input('Digite o nome do jogador: ').lstrip().rstrip()
    tot_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    # Para cada partida (p) no range de 0 até o total de partidas:
    for p in range(tot_partidas):
        # p+1, pois não queremos mostrar "partida 0", por exemplo, e sim, "partida 1":
        gols.append(int(input(f'  Quantos gols na partida {p+1}? ')))
    # Os elementos da lista gols são passados para o item 'Gols' do dicionário:
    jogador['Gols'] = gols[:]
    # O item 'Total' do dicionário recebe a soma da lista gols:
    jogador['Total'] = sum(gols)
    
    # time recebe a cópia dos valores dentro de jogador:
    time.append(jogador.copy())
    # jogador é zerado:
    jogador.clear()
    # gols é zerado:
    gols.clear()

    resp = ''
    # Enquanto resp for uma string vazia, ou não estiver dentro das opções disponíveis ('SN'):
    while not resp or resp[0] not in 'SN':
        resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
    
print('-='*30)

print('TIME DE FUTEBOL')
print('-'*120)
# Mostra o num, nome, gols e total da tabela, cada um com seus determinados espaços:
print(f'{'NÚM':<6}{'NOME':<40}{'GOLS':<60}{'TOTAL'}')
print('-'*120)
# Para cada jogador dentro de time, sendo que i é o índice do jogador:
for i, jogadores in enumerate(time):
    # Mostra o índice do jogador + 1, pois não queremos que ele mostre "num 0", e sim, "num 1". Mostra o nome do jogador atual,
    # sendo limitado à 30 caracteres com o [:30], para que ele não ocupe o espaço das outras categorias se ele for muito longo, 
    # os gols dele (Transformamos a lista de gols em strings para que os elementos sejam exibidos sem os colchetes, 
    # e que possam ser alinhados numa quantidade de caracteres com o :<60), e por fim, mostra o total de gols do jogador atual:
    print(f'{i+1:<6}{jogadores["Nome"][:30]:<40}{', '.join(map(str, jogadores["Gols"])):<60}{jogadores["Total"]}')

while True:
    print('-'*40)
    opc = int(input('Mostrar dados de qual jogador? (Digite o NUM do jogador. -1 para mostrar a tabela novamente, -2 para parar): '))
    
    if 0 < opc <= len(time):
        # Aqui e em outras partes do código, eu coloquei opc - 1, pois os NÚMs dos jogadores começam no 1, e o enumerate começa no 0:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[opc - 1]["Nome"].upper()}:')
        # Para cada gol dentro da lista de gols, sendo que i é o índice de cada gol/partida:
        for i, gol in enumerate(time[opc - 1]['Gols']):
            # i+1 pois não queremos que mostre "jogo 0", e sim, "jogo 1", mostra o nome do jogador escolhido pelo opc - 1 o gol da partida atual:
            print(f'      No jogo {i+1}, {time[opc - 1]["Nome"]} fez {gol} gol(s).')
        # Mostra o total de gols do jogador que foi escolhido pelo opc - 1:
        print(f'      Resultando assim, num total de {time[opc - 1]["Total"]} gol(s).')
            
    elif opc == -1:
        # Mostra a tabela novamente, eu poderia fazer uma função para a exibição da tabela, mas ainda não aprendi isso:
        print('TIME DE FUTEBOL')
        print('-'*120)
        print(f'{'NÚM':<6}{'NOME':<40}{'GOLS':<60}{'TOTAL'}')
        print('-'*120)
        for i, jogadores in enumerate(time):
            print(f'{i+1:<6}{jogadores["Nome"][:30]:<40}{', '.join(map(str, jogadores["Gols"])):<60}{jogadores["Total"]}')
            
    elif opc == -2:
        break
    
    else:
        print('Número de jogador inválido! Na esquerda dos nomes dos jogadores na tabela, tem os números deles. Por favor, tente novamente com eles.')

print('-='*30)
print('TIME FORMADO! VOLTE SEMPRE!')
