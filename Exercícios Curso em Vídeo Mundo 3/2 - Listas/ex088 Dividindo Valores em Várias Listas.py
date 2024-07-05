print('-'*30)
print(f'{'LISTAS':^30}')
print('-'*30)

num = []
par = []
imp = []
while True:
    num.append(int(input('Digite um número: ')))
    r = ''
    # Enquanto r for uma string vazia, ou seu primeiro caractere não estiver dentro das opções disponíveis ('SsNn'):
    while not r or r[0] not in 'SsNn':
        r = input('Deseja continuar? [S/N]: ').strip()
    if r[0] in 'Nn':
        break

# Para cada valor dentro da lista num:
for v in num:
    # Faz a verificação se o número é PAR ou ÍMPAR, e adiciona cada um deles às suas respectivas listas:
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)

print('-='*30)
num.sort() # Ordena a lista em ordem crescente
print('A lista COMPLETA E ORDENADA ficou assim: ', end='')
# join separa cada elemento (menos o último, por isso o + '.' no final) da lista, o separador, nesse caso, vai ser a vírgula. Como o join só funciona em strings, map treansforma
# todos os elementos dentro da lista em strings em todos os casos (Lista completa, Lista dos Pares e Lista dos Ímpares):
print(', '.join(map(str, num)) + '.')

print('A lista dos números PARES ficou assim: ', end='')
print(', '.join(map(str, par)) + '.')

print('A lista dos números ÍMPARES ficou assim: ', end='')
print(', '.join(map(str, imp)) + '.')

print('-'*30)
print('FIM DO SOFTWARE!\n')