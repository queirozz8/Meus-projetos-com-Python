print('-'*30)
print(f'{'LISTAS':^30}')
print('-'*30)

num = []
while True:
    n = int(input('Digite um número para a sua lista: '))
    # Se o número que o usuário digitou não estiver dentro da lista, quer dizer que esse número ainda não foi adicionado, então:
    if n not in num:
        # Adiciona o valor atual que o usuário digitou para a lista:
        num.append(n)
        print('Valor adicionado!')
    # Se o número que o usuário digitou estiver dentro da lista, quer dizer que esse número já foi adicionado, então:
    else:
        # Não adiciona:
        print('Este valor já existe na lista! Não vou adicionar.')
    
    # map() aplica uma função em cada novo elemento da estrutura de dados, no caso, estamos pedindo para que ele transforme todos os números em str, para que assim o join() 
    # funcione, e aplique o separador (', ') em cada elemento, com exceção do último (Pois é assim que o join() funciona), como ele não adiciona o separador no último número, 
    # concatene o último número com a str '.', para que o output seja corretamente mostrado ao usuário:
    num_ordenados = ', '.join(map(str, sorted(num))) + '.'
    print(f'Sua lista está assim: {num_ordenados}')
    # A resposta do usuário previamente começa vazia, se o usuário falar que quer continuar, quando ele chegar aqui a resposta dele vai reiniciar, para assim o software perguntar
    # novamente ao usuário se ele quer continuar:
    resp = ''
    # Enquanto a resposta do usuário for uma string vazia, ou o primeiro caractere da resposta do usuário não estiver dentro da tupla de opções disponíveis ('SsNn'):
    while not resp or resp[0] not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
    
print(f'Fim do Software! Sua lista ficou assim: {num_ordenados}')
