print('='*30)
print(f'{'LISTAS':^30}')
print('='*30)
valores = []
for cont in range(5):
    valores.append(float(input(f'Digite um número para o valor {cont} da lista: ')))
print('-='*30)
print(f'Sua lista ficou assim: {valores}')

# MAIOR
# max() retorna o maior valor da lista e atribui o retorno à variável maior:
maior = max(valores)
cont_maior = 0
print(f'O MAIOR valor da lista foi {maior}, na(s) posição(ões): ',end='')
# Descobrindo quantos maiores valores existem:
# Para cada valor na lista valores:
for valor_atual in valores:
    # Se o valor atual for o maior número:
    if valor_atual == maior:
        # Então o contador de maiores números recebe +1:
        cont_maior += 1
# Para cada valor atual na lista valores, só que agora os índices dos valores atuais também são contados com o enumerate():
for ind_maior, valor_atual in enumerate(valores):
    # Se o valor atual for o maior:
    if valor_atual == maior:
        if cont_maior > 1:
            # Mostra o número com uma vírgula no final, pois mais números estão por vir:
            print(f'{ind_maior},', end=' ')
            # Remove 1 do contador, até chegar em 1, que o for loop vai executar o else:
            cont_maior -= 1
        else:
            # Mostra o número com um ponto final e pulando a linha normalmente, pois esse é o último número:
            print(f'{ind_maior}.')

# MENOR
# min() retorna o menor valor da lista e atribui o retorno à variável menor:
menor = min(valores) 
cont_menor = 0
print(f'O MENOR valor da lista foi {menor}, na(s) posição(ões): ', end='')
# Descobrindo quantos menores valores existem:
# Para cada valor atual na lista valores:
for valor_atual in valores:
    # Se o valor atual for o menor:
    if valor_atual == menor:
        # Então o contador de menores números recebe +1:
        cont_menor += 1
# Para cada valor atual na lista valores, só que agora os índices dos valores atuais também são contados com o enumerate():
for ind_menor, valor_atual in enumerate(valores):
    # Se o valor atual for o menor:
    if valor_atual == menor:
        if cont_menor > 1:
            # Mostra o número com uma vírgula no final, pois mais números estão por vir:
            print(f'{ind_menor},', end=' ')
            # Remove 1 do contador, até chegar em 1, que o for loop vai executar o else:
            cont_menor -= 1
        else:
            # Mostra o número com um ponto final e pulando a linha normalmente, pois esse é o último número:
            print(f'{ind_menor}.')
print('-='*30)
# LISTA ORDENADA
print(f'Sua lista com os NÚMEROS DESTACADOS e ORDENADA ficou assim (Números \033[32mVERDES\033[m são os MENORES, \033[31mVERMELHOS\033[m são os MAIORES):')
# Organiza os valores do menor para o maior:
valores.sort()
# Para cada valor da lista valores:
for cont, valor in enumerate(valores):
    # Se o valor for o maior:
    if valor == maior:
        # Mostra o valor atual (Que é o maior número), só que agora em vermelho (\33[31m{valor}) e termina a coloração avermelhada (\033[m)
        print(f'\033[31m{valor}\033[m', end='')
        if cont != 4:
            print(',', end=' ')
        else:
            print('.')

    # Caso contrário, se o valor for o menor:
    elif valor == menor:
        # Mostra o valor atual (Que é o menor número), só que agora em verde (\033[32m{valor}) e termina a coloração esverdeada (\033[m):
        print(f'\033[32m{valor}\033[m', end='')
        # Se o valor não for o último:
        if cont != 4:
            # Mostra uma vírgula e um espaço no final, para o próximo número vir (Já que o número atual (valor) não é o último, como a linha acima acabou de verificar)
            print(',', end=' ')
        # Caso contrário, se o valor atual for o último:
        else:
            # Mostre um ponto final. Sem espaços nem nada, já que esse é o último número:
            print('.')
    # Caso contrário, se o valor atual não for nem o menor nem o maior número:
    else:
        # Mostra o valor atual normalmente, sem cores nem nada:
        print(f'{valor}', end='')
        # Se o valor não for o último:
        if cont != 5:
            # Mostra uma vírgula e um espaço no final, para o próximo número vir (Já que o número atual (valor) não é o último, como a linha acima acabou de verificar)
            print(',', end=' ')
        # Caso contrário, se o valor atual for o último:
        else:
            # Mostre um ponto final. Sem espaços nem nada, já uqe esse é o último número:
            print('.')
    # Como os valores são mostrados de forma avulsa, não em uma lista, os valores já saem sem os colchetes [], facilitando a leitura do usuário dos números.
print('-'*40)
print('FIM DO SOFTWARE!')
