def leia_int(input_):
    while True:
        r = input(input_)
        if r.isnumeric():
            print(f'\033[32mVocê digitou o número inteiro {r}, o que está correto.\033[m')
            break
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
            
leia_int('Digite um número inteiro (A proposta é dar uma mensagem de erro caso você digite algo que não seja um número): ')