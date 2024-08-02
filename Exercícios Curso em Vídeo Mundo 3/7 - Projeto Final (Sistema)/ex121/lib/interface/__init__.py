def leia_int(msg):
    """
    -> Lê um número inteiro.
    Possui tratamento de exceções, para que ele só aceite números inteiros digitados pelo usuário.
    """
    
    while True:
        try:
            i = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um NÚMERO INTEIRO!\033[m')
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário decidiu não informar o número inteiro.\033[m')
            return '<número não informado>'
        else:
            break
    return i


def cabecalho(txt):
    """
    ->
    Cria um cabeçalho/título.
    Usa a função linha, que mostra uma linha com um padrão de 42 caracteres.
    """
    
    linha()
    print(f'{txt}'.center(42))
    linha()


def linha(tam=42):
    print('='*tam)


def menu(lista):
    """
    -> Cria um menu na tela.
    lista é a lista de opções que menu vai receber.
    Mostra os elementos de lista e sua numeração, para o usuário digitar o número da opção.
    Pergunta a opção do usuário, e retorna a opção digitada pelo usuário.
    """
    
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{item}\033[m')
    opc = leia_int('\033[32mSua Opção: \033[m')
    return opc
