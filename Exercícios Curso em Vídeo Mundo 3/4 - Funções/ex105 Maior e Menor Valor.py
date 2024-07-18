from time import sleep


# Aqui, num vai ser uma lista de valores, ele não vai ter uma determinada quantidade de parâmetros que vão ser passados, ele vai ter quantos parâmetros forem
def maior_menor(*num):
    maior = menor = 0
    
    print('-'*20)
    print(f'Analisando o(s) número(s)...', end=' ')
    for numero in num:
        # Usei o flush para o Python não fazer buffering do sleep, e sim, mostrar cada número com um certo intervalo de tempo:
        print(numero, end=', ', flush=True)
        sleep(0.3)
    print(f'foi(ram) informado(s) {len(num)} número(s) ao todo.')

    for numero in num:
        # Verificação do MAIOR número:
        if numero > maior:
            maior = numero

        # Verificação do MENOR número
        if numero == 0:
            menor = numero
        if numero < menor:
            menor = numero
    print(f'O MAIOR número é {maior}.')
    print(f'O MENOR número é {menor}.')


# Programa Principal, coloquei alguns exemplos. Caso alguma outra pessoa esteja vendo isso, você pode mudar os valores, contanto que seja um número int ou float:
maior_menor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior_menor(43,11,25,561,546,312,345,61,94)
maior_menor(5,42,3,4,6,6,7,67,567,56,345,435,56,7,2,34,123,789,348267,345978,128376,456)
maior_menor(-5,-4,-3,-2,-1,0,1,2,3,4,5)
maior_menor(1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0)
maior_menor(0)
maior_menor()
