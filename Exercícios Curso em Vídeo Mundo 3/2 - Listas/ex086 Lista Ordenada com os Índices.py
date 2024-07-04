print('-'*30)
print(f'{'LISTAS':^30}')
print('-'*30)

numeros = []
print('Irei te perguntar 5 números ↓')
for i in range(1, 6):
    n = int(input(f'\nDigite o {i}° número: '))
    # Se o número digitado pelo usuário for o primeiro número de todos, ou se o número digitado pelo usuário for maior do que o último número:
    if i == 1 or n > numeros[-1]:
        numeros.append(n)
        print(f'Valor {n} adicionado ao final da lista.')
    else:
        pos = 0
        # Enquanto pos (Posição que estamos da lista números) for menor ou igual ao tamanho de numeros:
        while pos <= len(numeros):
            # Se n for menor ou igual ao número da posição que estamos atualmente:
            if n <= numeros[pos]:
                # Insere o número atual do usuário, na posição do número anterior, ou seja, ele toma o lugar do número que está na posição pos:
                numeros.insert(pos, n)
                print(f'Valor {n} adicionado na posição {pos} da lista.')
                break
            pos += 1
    
    if i < 5:
        # join coloca para que todos os números sejam separados por ', ', menos o último número (Ele não vai ter , no final). map(str, numeros) transforma cada número novo da 
        # lista em uma string, para que o join() possa funcionar corretamente:
        print(f'Como a lista ordenada está nesse momento: {', '.join(map(str, numeros))}.')
print(f'\nFim do Software! Sua lista ordenada ficou assim: {', '.join(map(str, numeros))}.')
