print('-'*30)
print(f'{'MATRIZ (V1)':^30}')
print('-'*30)

# Criamos a matriz. Cada sub-lista é uma coluna, cada elemento das colunas são as linhas/elemento:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# i é o índice da coluna atual. Para cada coluna dentro da matriz:
for i, coluna in enumerate(matriz):
    # elemento é o índice do elemento dentro da coluna atual:
    for elemento, _ in enumerate(coluna):
        # O que o usuário digitar vai modificar os elementos (quem define qual elemento vai ser modificado é a variável elemento) dentro da coluna [i]. 
        matriz[i][elemento] = int(input(f'Digite um número inteiro para [{i}, {elemento}]: '))
print('-'*30)
print('Sua matriz 3x3 ficou assim:\n')
# Para cada coluna na matriz:
for coluna in matriz:
    # Para cada elemento na coluna:
    for elemento in coluna:
        # Mostre o elemento centralizado em 5 caracteres:
        print(f'[{elemento:^5}] ', end='')
    print()
print('-'*30)
print('FIM DO SOFTWARE!')