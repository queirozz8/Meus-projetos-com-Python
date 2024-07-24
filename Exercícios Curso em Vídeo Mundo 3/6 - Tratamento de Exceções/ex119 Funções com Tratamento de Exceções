# INTEIRO
def leia_int():
    while True:
        try:
            i = int(input('Digite um NÚMERO INTEIRO: '))        
        except(TypeError, ValueError):
            print('\033[031mERRO: Digite um NÚMERO INTEIRO válido.\033[m')
        except(KeyboardInterrupt):
            print('\n\033[031mO usuário preferiu não digitar o número inteiro.\033[m')
            return '<número não digitado>'
        else:
            return i

# FLOAT
def leia_float():
    while True:
        try:
            f = float(input('Digite um NÚMERO FLOAT (Número Racional, número com ponto, número real) (Se você digitar um número inteiro, será transformado em float): '))
        except(TypeError, ValueError):
            print('\033[031mERRO: Digite um NÚMERO FLOAT válido.\033[m')
        except(KeyboardInterrupt):
            print('\n\033[031mO usuário preferiu não digitar o número float.\033[m')
            return '<número não digitado>'
        else:
            return f
        
# Programa Principal
print('-'*70)
print('LEIA INT E LEIA FLOAT COM TRATAMENTO DE ERROS'.center(70))
print('Tente errar na digitação dos valores.'.center(70)) 
print('Aperte Ctrl + C para não digitar o valor atual e passar para o próximo.'.center(70))
print('-'*70)

n1 = leia_int()
n2 = leia_float()
print(f'O NÚMERO INTEIRO digitado foi {n1} e o NÚMERO FLOAT digitado foi {n2}.')
print('\nFIM DO SOFTWARE!\n')
