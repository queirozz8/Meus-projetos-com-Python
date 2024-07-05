print('-'*30)
print(f'{'LISTAS':^30}')
print('-'*30)

num = []
while True:
    num.append(int(input('\nDigite um número: ')))
    r = ''
    # Enquanto a variável r for uma string vazia, ou r[0] não estiver dentro das opções permitidas ('SsNn'):
    while not r or r[0] not in 'SsNn':
        r = input('Deseja continuar? [S/N]: ').strip()
    if r[0] in 'Nn':
        break

print('-='*30)
print('Sua lista ficou assim: ', end='')
# Para cada número dentro do tamanho da lista num:
for i in range(len(num)):
    # Mostre o elemento da lista num, só que na posição que o número i estiver:
    print(num[i], end='')
    # Se o contador (i) for menor do que o tamanho da lista (Não é o último número):
    if i < len(num) - 1:
        # Mostre uma vírgula, até porque mais números estão por vir: 
        print(', ', end='')
    # Caso contrário, se i for do tamanho da lista, isso é, se for o último valor, mostre um ponto final, até porque esse é o último número:
    else:
        print('.')
print(f'{len(num)} número(s) foi(foram) digitado(s). ')
num.sort() # Organiza a lista em ordem crescente
print(f'Número(s) organizado(s) em ordem crescente: {num}')
num.sort(reverse=True) # Organiza a lista em ordem decrescente
# join junta os números e separa eles por uma ', '. Map transforma todos os valores da lista em strings separadas, para que o join funcione corretamente:
print(f'Número(s) oganizado(s) em ordem decrescente: {', '.join(map(str, num))}.')
# Se tiver mais de 0 números 5:
if num.count(5) > 0:
    print(f'O número 5 foi digitado {num.count(5)} vezes.')
else:
    print('O número 5 não foi digitado na sua lista!')

print('-'*30)
print('FIM DO SOFTWARE!')
