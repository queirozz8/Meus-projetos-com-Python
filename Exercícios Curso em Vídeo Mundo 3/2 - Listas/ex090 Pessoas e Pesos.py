print('-'*80)
print(f'{'ANALISADOR DE PESSOAS E PESOS':^80}')
print(f'{'Digite o nome de uma pessoa, seu peso e eu farei as análises no final.':^80}')
print('-'*80)
# temp é uma lista temporária, ela existe para verificar os maiores e menores números que o usuário digitou. Depois de analisar, ela manda os dados para a lista principal (princ)
# e apaga todos os dados que existem nela (clear):
temp = []
# princ é a lista principal, é a que vamos manipular:
princ = []
mai = men = 0

while True:
    temp.append(input('Nome: ').lstrip())
    temp.append(float(input('Peso: ')))
    # Se o valor que o usuário digitou foi o primeiro de todos:
    if len(princ) == 0:
        # mai e men é esse valor:
        mai = men = temp[1]
    else:
        # Se o peso que o usuário digitou é maior do que o maior número anterior:
        if temp[1] > mai:
            # O maior número agora se torna o peso que o usuário colocou atualmente:
            mai = temp[1]
        # Se o peso que o usuário digitou é menor do que o menor número anterior:
        if temp[1] < men:
            # O menor número agora se torna o peso que o usuário colocou atualmente:
            men = temp[1]
    # Manda os dados (Nome da pessoa e o peso dela) para a lista principal (princ):
    princ.append(temp[:])
    # Apaga todos os dados da lista, para assim ela receber mais um nome e peso de outra pessoa e passar para a lista principal:
    temp.clear()
    
    resp = ''
    # Enquanto resposta for uma string vazia ou o primeiro caractere dela não estiver dentro das opções disponíveis ('SsNn'):
    while not resp or resp[0] not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip()
    if resp[0] in 'Nn':
        break

print('-='*60)
# TODAS AS PESSOAS E SEUS PESOS
# len(princ) mostra quantos elementos aquela lista tem:
print(f'Você digitou {len(princ)} pessoas:')
for n, p in enumerate(princ):
    # n começa com 0, então somamos +1 para exibir corretamente. p[0] são os nomes de todas as sub-listas que estão dentro da princ. p[1] são todos os pesos de todas as pessoas.
    print(f'{n+1}° Pessoa: {p[0]} - Peso: {p[1]}.')

# MAIORES PESOS
print(f'O MAIOR peso digitado foi {mai}Kg. Peso de ', end='')
maiores = []
# Para cada pessoa dentro de princ:
for p in princ:
    # Se o peso for o maior peso:
    if p[1] == mai:
        # Adiciona o nome da pessoa dentro da lista maiores. No final, a lista maiores fica com todos os nomes das pessoas mais pesadas:
        maiores.append(p[0])
# Para cada nome das pessoas dentro da lista maiores:
for i, nome in enumerate(maiores):
    # Mostre o nome da pessoa (Não tem peso na lista maiores, só os nomes, a variável nome passa por todos os nomes dentro da lista maiores):
    print(nome, end='')
    # Se o índice de cada nome for menor do que o tamanho da lista maiores - 1 (- 1 pois queremos desconsiderar a última pessoa da lista, para mostrarmos um ponto final). 
    """Basicamente, vamos supor que maiores/menores é uma lista com 5 pessoas. len(maiores/menores) - 1 = 4. O enumerate vai funcionar assim:
    0 < 4. Mostre ', '
    1 < 4. Mostre ', '
    2 < 4. Mostre ', '
    3 < 4. Mostre ', '
    4 = 4 (É o último número da lista). Mostre '.' """
    if i < len(maiores) - 1:
        print(', ', end='')
    else:
        print('.')

# MENORES PESOS
print(f'O MENOR peso digitado foi {men}Kg. Peso de ', end='')
menores = []
# Para cada pessoa dentro de princ:
for p in princ:
    # Se o peso for o maior peso:
    if p[1] == men:
        # Adiciona o nome da pessoa dentro da lista menores. No final, a lista menores fica com todos os nomes das pessoas mais leves:
        menores.append(p[0])
# Para cada nome das pessoas dentro da lista maiores:
for i, nome in enumerate(menores):
    # Mostre o nome da pessoa (Não tem peso na lista menores, só os nomes, a variável nome passa por todos os nomes dentro da lista maiores):
    print(nome, end='')
    # Se o índice de cada nome for menor do que o tamanho da lista menores - 1 (-1 pois queremos desconsiderar a última pessoa da lista, para mostrarmos um ponto final).
    # A explicação dessa linha de código eu expliquei na parte das pessoas com maiores pesos:
    if i < len(menores) - 1:
        print(', ', end='')
    else:
        print('.')

print('-'*80)
print('FIM DO SOFTWARE!')