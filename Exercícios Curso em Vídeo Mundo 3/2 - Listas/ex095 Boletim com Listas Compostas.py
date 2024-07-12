print('-'*30)
print(f'{'BOLETIM DE ALUNOS':^30}')
# ficha é a lista principal. Nela, cada aluno vai estar em uma sub-lista, com uma outra sub-lista dentro, onde ficam suas notas, e o último elemento, que é a média:
ficha = []
while True:
    print('-'*30)
    nome = input('Digite o nome do aluno: ').lstrip().rstrip()
    nota_1 = float(input('Digite a primeira nota do aluno: '))
    nota_2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    r = ''
    # Enquanto r for uma string vazia ou não estiver dentro das opções disponíveis ('SsNn'):
    while not r or r[0] not in 'SsNn':
        r = input('Deseja continuar? [S/N]: ').strip()
    if r[0] in 'Nn':
        break

print('-'*30)
print(f'{'BOLETIM':^30}')
print('-'*30)
print(f'{'N°':<4}{'NOME':<15}{'MÉDIA':>9}')
print('-'*30)
# Para cada aluno na ficha, sendo que ind_aluno é o índice do aluno:
for ind_aluno, aluno in enumerate(ficha):
    # Mostre o índice do aluno + 1 (enumerate trabalha começando com 0, para deixar mais fácil para os usuários, adicionamos +1 para que o primeiro aluno seja 1, não 0), o
    # elemento  0 (que representa o nome dele) (O aluno que ele deve mostrar é ordenado pela variável aluno), e por fim o elemento 2 (a média dele):
    print(f'{ind_aluno + 1:<4}{aluno[0]:<15}{aluno[2]:>9.2f}')

while True:
    print('-'*30)
    opc = int(input('Qual aluno deseja ver as notas? (Digite o NÚMERO DO ALUNO. Digite -1 para VER O BOLETIM NOVAMENTE. Digite -2 para PARAR.): '))
    if 0 < opc <= len(ficha):
        # Como as listas começam no 0, colocamos - 1 para que o índice esteja correto novamente, pois na verdade o usuário está digitando  o valor "errado" do aluno que 
        # ele quer  ver, vamos supor que ele quer ver o primeiro aluno (que é 0, porém mostramos 1), quando  ele digita 1, os dados do aluno que o software passaria 
        # seriam do aluno errado. Então corrigimos isso com o [opc - 1]:
        print(f'As notas de {ficha[opc - 1][0]} são ', end='')
        # Separe cada elemento da lista por vírgulas (transforme todos os elementos em strings para que isso funcione), mostre a média do aluno (Mesma técnica do - 1 já 
        # explicada anteriormente):
        print(', '.join(map(str, ficha[opc - 1][1])) + f', a média é {ficha[opc - 1][2]}', end='. ')
        # Se a média do aluno for igual ou maior que 6, então ele passou:
        if ficha[opc - 1][2] >= 6:
            print('Como esse estudante tirou mais que 6, então ele PASSOU.')
        # Se a média do aluno for 5, então ele ficou de recuperação:
        elif ficha[opc - 1][2] == 5:
            print('Como esse estudante tirou 5, ele está de RECUPERAÇÃO.')
        # Se a média do aluno for menor que 5, então ele reprovou:
        else:
            print('Como esse estudante tirou menos que 5, ele está REPROVADO.')
    
    # Se o usuário escolher que quer mostrar o boletim novamente:
    if opc == -1:
        print('-'*30)
        print(f'{'BOLETIM':^30}')
        print('-'*30)
        print(f'{'N°':<4}{'NOME':<15}{'MÉDIA':>9}')
        print('-'*30)
        for ind_aluno, aluno in enumerate(ficha):
            print(f'{ind_aluno + 1:<4}{aluno[0]:<15}{aluno[2]:>9.2f}')
    
    # Se o usuário escolher sair:
    if opc == -2:
        break

print('-'*30)
print('>>> OBRIGADO, VOLTE SEMPRE! <<<\n')
