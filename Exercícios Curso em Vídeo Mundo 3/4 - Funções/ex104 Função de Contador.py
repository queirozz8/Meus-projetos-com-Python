from time import sleep


def contador(i, f, p):
    # Se o passo que o usuário digitar for um número negativo, invertemos o sinal, tornando-o positivo:
    if p < 0:
        p *= -1
    # Se o passo que o usuário digitar for igual à 0, o que não faz sentido, o passo se torna 1:
    if p == 0:
        print('Passo 0 não faz sentido! Vamos de 1 em 1 então.')
        p = 1
    
    print('-'*20)
    print(f'Contando {i} até {f} de {p} em {p}: ')
    sleep(1)
    
    # Se a ordem for crescente:
    if i < f:
        cont = i
        while cont <= f:
            # Usei o flush=True para o Python não fazer buffer do sleep, e sim, mostrar cada valor unicamente, e depois ter um delay de 0.3 segundos:
            print(cont, end=', ', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    # Se a ordem for decrescente:
    else:
        cont = i
        while cont >= f:
            print(cont, end=', ', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')


# Programa Principal
print('-'*20)
print(f'{'CONTADOR COM FUNÇÕES':^20}')

contador(1, 10, 1)
contador(10, 0, 2)

# Contagem personalizada:
print('Agora chegou sua vez de personalizar essa contagem!')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passos (Números negativos serão invertidos o sinal, e se for 0, automaticamente vira 1):  '))
# Chamamos a função, agora com os parâmetros que o usuário digitou:
contador(ini, fim, pas)