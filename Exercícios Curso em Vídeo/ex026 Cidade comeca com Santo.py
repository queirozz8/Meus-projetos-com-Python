nome_cidade = str(input('Digite o nome de uma cidade: '))
comecacomsanto = nome_cidade[:5].lower() == 'santo' and len(nome_cidade) > 6
print('O nome da sua cidade começa com a palavra Santo? {}'.format(comecacomsanto))