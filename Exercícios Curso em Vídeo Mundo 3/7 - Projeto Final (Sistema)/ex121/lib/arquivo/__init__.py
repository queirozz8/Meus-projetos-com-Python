from lib.interface import *


def arquivo_existe(nome):
    """
    -> Verifica se um arquivo existe.
    Ela tenta abrir o arquivo de texto em modo de leitura, depois fecha ele. Caso ela consiga fazer isso, ela retorna True, caso contrário, ela retorna False.
    """
    
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto.
    Ela tenta criar o arquivo de texto, caso ela não consiga, ela retorna uma mensagem de erro. Caso consiga, ela avisa que o arquivo foi criado.
    """
    
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso para o funcionamento do software!')
  
        
def ler_arquivo(nome):
    """
    -> Lê um arquivo de texto.
    Ela tenta abrir o arquivo de texto, caso ela não consiga, ela retorna uma mensagem de erro. Caso consiga, ela mostra as linhas do arquivo.
    """
    
    try:
        a = open(nome, 'rt')
    except:
        print(f'ERRO na leitura do arquivo de texto {nome}!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(f'{'N°':<3}{'NOME':<34}{'IDADE'}')
        print('-'*42)
        for i, linha in enumerate(a):
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{i+1:<3}{dado[0][:33]:<34}{dado[1][:4]}')
    finally:
        a.close()
        
        
def cadastrar(arq, nome='<desconhecido>', idade=0):
    """
    -> Cadastra uma nova pessoa em dados.txt.
    Primeiro, ele tenta abrir o arquivo em modo de append;
    caso consiga, ele tenta escrever o nome e a idade que o usuário forneceu;
    caso consiga, ele mostra que conseguiu fazer o novo registro da pessoa, e fecha o arquivo.
    """
    
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        if nome == '':
            nome = '<desconhecido>'
        if idade == '<número não informado>':
            idade = 0

        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome[:33]} adicionado.')
            a.close()
