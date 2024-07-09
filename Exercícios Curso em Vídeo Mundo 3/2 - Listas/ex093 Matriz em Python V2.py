print('-'*60)
print(f'{'MATRIZ (V2)':^60}')
print(f'{'Colunas são verticais, linhas são horizontais nessa matriz':^60}')
print('-'*60)

# Criamos a matriz. Cada sub-lista é uma linha; como cada linha tem 3 elementos, colocamos 3 zeros em cada uma; os inputs do usuário irão mudar esses valores:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# pares é a lista onde todos os números pares serão armazenados para serem somados depois:
pares = []
# soma_terceira_coluna é a lista onde todo último elemento das linhas vai ser armazenado para ser somado depois:
soma_terceira_coluna = []
# Para cada linha na matriz: (i_linha é o índice da linha)
for i_linha, linha in enumerate(matriz):
    # elemento é o índice de cada elemento da linha:
    for elemento, _ in enumerate(linha):
        # O que o usuário digitar vai ser atribuído ao elemento atual da linha, a linha é determinada pelo i_linha:
        matriz[i_linha][elemento] = int(input(f'Digite um número inteiro para a posição [{i_linha}, {elemento}]: '))

print('-'*40)
print('Sua matriz 3x3 ficou assim:\n')
# Para cada linha na matriz:
for linha in matriz:
    # soma_terceira_coluna recebe o último elemento de cada linha:
    soma_terceira_coluna.append(linha[2])
    # para cada elemento da linha:
    for elemento in linha:
        # Se o elemento for par:
        if elemento % 2 == 0:
            # pares recebe o elemento para ser somado depois:
            pares.append(elemento)
        # Mostre o elemento atual centralizado em 5 caracteres.
        print(f'[{elemento:^5}] ', end='')
    # Depois de ter mostrado 3 elementos, pule uma linha:
    print()

print('-'*40)
print(f'A SOMA de todos os NÚMEROS PARES é {sum(pares)}.')

print('-'*40)
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA (Vertical) É {sum(soma_terceira_coluna)}.')

print('-'*40)
print(f'O MAIOR VALOR da SEGUNDA LINHA (Horizontal) é {max(matriz[1])}.\n')