def fatorial(n=1, show=False):
    from time import sleep
    """
    -> Calcula o fatorial de um número
    :param n: (Opcional, por padrão é 1) O número à ser calculado.
    :param show: (opcional, por padrão é False) Mostrar ou não a conta feita.
    """
    print('O fatorial é: ')
    f = 1
    for i in range(n, 0, -1):
        f *= i
        # Se show estiver como True, mostre a conta feita, então mostre o número atual (i), se o i for igual à 1 (Último número), você mostra "=", se não, mostre "x" mesmo: 
        if show:
            print(f'{i}', end=' ', flush=True)
            sleep(0.3)
            if i == 1:
                print(f'=', end=' ', flush=True)
                sleep(0.3)
            else:
                print('x', end=' ', flush=True)
                sleep(0.3)
    # Independente se show estiver como True ou False, a função vai retornar o valor de f:
    return f
        
# Programa Principal
print(fatorial(5, True), end='.')
