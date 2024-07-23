def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[031mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
