from datetime import datetime

print('-='*30)
print('CADASTRO DE TRABALHADOR')
print('-='*30)

dados = {}
# Adicionamos a chave 'Nome' no dicionário dados, que vai armazenar o nome que o usuário digitar (Espaços no início e no final vão ser removidos):
dados['Nome'] = input('Nome: ').lstrip().rstrip()
nasc = int(input('Ano de Nascimento (Não é a idade, é o ano de nascimento): '))
# Primeiro recebemos o ano de nascimento para calcular a idade depois. Criamos a chave 'Idade' que recebe o ano atual - ano de nascimento:
dados['Idade'] = datetime.now().year - nasc
dados['Ctps'] = int(input('Carteira de Trabalho (Se não tiver, digite 0): '))
# Se o usuário tiver Carteira de Trabalho:
if dados['Ctps'] != 0:
    # Pegamos o ano de contratação, criamos uma chave para armazenar esse valor:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    # A mesma coisa para o salário:
    dados['Salário'] = float(input('Salário: R$'))
    # Em Aposentadoria, fazemos um cálculo: a idade (previamente calculada) + o ano de contratação + 35 - ano atual. 35 foi o ano que o professor do curso estipulou
    # para ser o ano em que os trabalhadores aposentam. Existe a diferença do tanto de anos que a pessoa precisa trabalhar para se aposentar baseada no gênero de cada pessoa, 
    # porém nesse exercício não estamos considerando ela.
    dados['Aposentadoria'] = dados['Idade'] + dados['Contratação'] + 35 - datetime.now().year

print('-='*30)
# Para cada chave, valor em dados:
for k, v in dados.items():
    # Primeiro, mostre a chave sozinha, sem pular a linha. Pois nós iremos fazer umas análises de dados antes de mostrar os valores:
    print(f'{k}: ', end='')
    
    # Se a chave atual for a de Salário:
    if k == 'Salário':
        # Mostre o salário de forma formatada, com vírgulas para separar valores maiores e com 2 casas depois da vírgula:
        print(f'R${v:,.2f}.', end='')
    # Caso não for o salário: Estou fazendo essa verificação só com o salário pois ele é o único valor que sai de uma forma diferente dos outros valores:
    else:
        # Mostre o valor normalmente, com um espaço no final pois vamos analisar outras coisas ainda:
        print(f'{v}.', end=' ')

    # Se a chave atual for a de Carteira de Trabalho:
    if k == 'Ctps':
        # Se o valor dentro dessa chave for 0 (Quer dizer que o usuário não possui carteira de trabalho):
        if dados['Ctps'] == 0:
            print('Não possui Carteira de Trabalho.')

    # Se a chave atual for a de Aposentadoria:
    if k == 'Aposentadoria':
        # O valor que está na chave de contratação é somado com 35, agora sabemos o ano que o usuário vai se aposentar, e mostramos para ele qual é o ano:
        print(f'Irá se aposentar no ano {dados["Contratação"] + 35}.')
    # Caso a chave não for a de Aposentadoria, pule uma linha: Só estou fazendo essa verificação com Aposentadoria pois ela é o único valor que sai sem pular uma linha:
    else:
        print()