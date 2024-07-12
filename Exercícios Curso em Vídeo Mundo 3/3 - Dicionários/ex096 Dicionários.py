aluno = {}
# Criamos a chave 'Nome', que armazena o valor que o usuário digitar:
aluno['Nome'] = input('Nome: ').lstrip().rstrip()
# Criamos a chave 'Média', que armazena o valor que o usuário digitar:
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    # Criamos a chave 'Situação' que armazena o valor 'Aprovado' se a média for maior ou igual à 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    # A mesma coisa para 'Recuperação' e 'Reprovado':
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*30)

# Para cada chave e valor dentro dos pares Chave-Valor que existem dentro do dicionário aluno:
for chave, valor in aluno.items():
    # Mostre a chave atual e o valor atual:
    print(f'  - {chave}: {valor}.')
