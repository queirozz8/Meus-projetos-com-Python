#EN: Requests the name of the city
#BR: Solicita o nome da cidade
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade começa com Santo? ')

#EN: Searches if the first 5 characters of the string begin with the word Santo. Put the entire name of the city in lowercase, to check without the risk of causing a bug
#BR: Procura se os primeiros 5 caracteres da string começam com a palavra Santo. Coloca o nome da cidade inteiro em minúsculo, para fazer a verificação sem tem risco de dar algum bug
print(cidade[:5].upper() == 'SANTO')
