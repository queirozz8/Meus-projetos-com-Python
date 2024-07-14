# pessoa é o dicionário que vai armazenar a pessoa atual que o usuário está cadastrando, vai ser enviado para galera, depois vai ser apagado para receber a próxima pessoa:
pessoa = {}
# galera vai ser a principal lista que vou estar manipulando aqui: 
galera = []
media = 0
while True:
    pessoa['Nome'] = input('Nome: ').lstrip().rstrip()

    while True:
        pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite M para Masculino, ou F para Feminino.')
    
    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']
    
    # Manda os elementos de pessoa para galera, fazendo uma cópia:
    galera.append(pessoa.copy())
    # Apaga o dicionário, para receber a possível próxima pessoa que o usuário digitar:
    pessoa.clear()

    resp = ''
    while not resp or resp[0] not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break

print('-='*30)
# Criei nomes_pessoas para adicionar todos os nomes das pessoas nela, fica melhor para filtrar:
nomes_pessoas = []
# Para cada nome (n) dentro da lista galera:
for n in galera:
    nomes_pessoas.append(n['Nome'])
print(f'AO TODO, temos {len(galera)} PESSOA(S) CADASTRADA(S). ', end='')
print(', '.join(nomes_pessoas) + '.')

# Calculamos a média, que é a soma de todos os números (Já feito anteriormente) dividido pelo número de algarismos (len(galera)):
media /= len(galera)
print(f'A MÉDIA DAS IDADES foi {media:.2f} anos.')

# Criei mulheres para adicionar todos os nomes das mulheres nela, fica melhor para filtrar:
mulheres = []
# Para cada mulher dentro da lista galera:
for m in galera:
    # Se o sexo daquela pessoa for Feminino:
    if m['Sexo'] == 'F':
        mulheres.append(m['Nome'])
print(f'Ao todo, temos {len(mulheres)} MULHER(ES) CADASTRADA(S). ', end='')
print(', '.join(mulheres) + '.')

# Criei galera_acima para adicionar todos os dados das pessoas que tem uma idade maior do que a média:
galera_acima = []
# Para cada pessoa dentro da lista galera:
for pessoas in galera:
    # Se a idade daquela pessoa for maior ou igual à media:
    if pessoas['Idade'] >= media:
        # Adiciona todos os dados daquela pessoa, não tem problema com o sexo ser um dado desnecessário, pois é só pegarmos as chaves desejadas:
        galera_acima.append(pessoas)
print(f'Ao todo, temos {len(galera_acima)} pessoas com uma IDADE ACIMA DA MÉDIA.', end=' ')
# Para cada pessoa dentro de galera_acima, sendo que i é o índice de cada pessoa:
for i, p in enumerate(galera_acima):
    # Mostra o valor da chave 'Nome' daquela pessoa, e faz a mesma coisa com a chave 'Idade':
    print(f'{p["Nome"]}, com {p["Idade"]} anos', end='')
    # i+1 porque o enumerate começa com 0, e o len começa com 1. Basicamente, se a pessoa mostrada for a última da lista, mostre um ponto final; se não, 
    # mostre uma vírgula e não pule a linha:
    if i+1 == len(galera_acima):
        print('.')
    else:
        print(',', end=' ')

print('\nFIM DO SOFTWARE!')