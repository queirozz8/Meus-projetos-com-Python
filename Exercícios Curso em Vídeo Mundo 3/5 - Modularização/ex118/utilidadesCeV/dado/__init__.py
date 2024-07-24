def leia_dinheiro(msg):
    valido = False
    while not valido:
        # A entrada do usuário é primeiramente lida como uma string, para que possamos substituir todas as ',' que o usuário digitar, por '.', para que o Python entenda:
        entrada = input(msg).strip().replace(',', '.')
        # Se a entrada do usuário for alfanumérica (Ou seja, tem alguma letra) ou for uma string vazia, exiba uma mensagem de erro na cor vermelha:
        if entrada.isalpha() or entrada == '':
            print(f'\033[031mERRO: "{entrada}" é um preço inválido!\033[m')
        # Caso contrário, se for realmente um número, então valido recebe True, e a função retorna a entrada, só que do tipo float agora:
        else:
            valido = True
            return float(entrada)
