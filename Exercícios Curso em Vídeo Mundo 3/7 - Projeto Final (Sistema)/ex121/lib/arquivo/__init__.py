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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:.<30}{dado[1]} anos')
    finally:
        a.close()
        
def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
