print('-'*100)
print(f'{'VERIFICADOR DE EXPRESSÕES MATEMÁTICAS':^100}')
print(f'''{'Irei verificar se a quantidade de parênteses que abem e fecham na sua expressão estão corretos':^100}''')
print('-'*100)
expr = input('Digite sua expressão matemática (Com parênteses): ')
# Pilha vai ser a lista que vai ter os caracteres de parênteses abertos '('. A lista pilha precisa estar vazia para a expressão ser correta
pilha = []
# Para cada caractere na expressão que o usuário digitou:
for c in expr:
    # Se o caractere é um parênteses abrindo:
    if c == '(':
        # Adiciona esse parênteses à pilha, precisamos encontrar um parênteses fechando para remover o parênteses 'pendente' que foi adicionado:
        pilha.append('(')
    # Caso o caractere seja um parênteses fechando:
    elif c == ')':
        # Se a pilha tiver mais que 0 elementos dentro dela:
        if len(pilha) > 0:
            pilha.pop() # Remove o último elemento da lista
            # O que fizemos aqui foi: Se o usuário colocou um '(' previamente e esse '(' foi para pilha, ele precisa ser removido, então olhamos os caracteres seguintes à procura
            # de um par para o '(' que foi adicionado. Se encontramos, então o último elemento da lista pilha (um parênteses) é removido com o pop().
        # Caso esse seja o primeiro elemento da lista, isso está errado, quem vem primeiro deve ser o parênteses abrindo, então:
        else:
            # Adicionamos o parênteses fechando
            pilha.append(')')
            # Saímos do for loop antes mesmo de ver os caracteres seguintes, pois isso já está errado: 
            break

print('-'*40)
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão não está correta! Cuidado com os PARÊNTESES...')