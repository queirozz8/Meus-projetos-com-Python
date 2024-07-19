def notas(*n, sit=False):
    """
    -> Função que informa o total de notas de um aluno, a maior e menor nota, a média, e se o usuário quiser, a situação também.
        n (tuple): Tupla que vai receber as notas dos alunos, é ela quem vai dar todas as informações que precisamos para mostrar a saída de volta ao usuário.
        sit (bool, optional): Padrão False, se for True, vai retornar a situação do aluno junto do dicionário também.

    Returns:
        Um dicionário contendo as informações do aluno
    """
    aluno = {}
    print(f'Notas recebidas: {n}.')
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    media = sum(n) / len(n)
    aluno['Média'] = media
    
    if sit:
        if media > 7:
            aluno['Situação'] = 'BOA'
        elif media > 5:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    
    return aluno

# Programa Principal
# Mude o sit para "False" caso não queria que o software mostre a situação do aluno:
resp = notas(5.5, 7.5, 6.3, 7.5, 2.3, 1.7, 7.4, sit=True)
print(resp)
help(notas)