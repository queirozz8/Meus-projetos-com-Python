import os
from lib.interface import *
from lib.arquivo import *
from time import sleep

# dir_atual recebe o caminho completo desse diretório:
dir_atual = os.path.dirname(__file__)
# arq recebe dir_atual junto com 'dados.txt', fazendo assim, o caminho completo para a criação do arquivo dados.txt:
arq = os.path.join(dir_atual, 'dados.txt')

# Se o arquivo (cursoemvideo.txt) não existe, crie o arquivo:
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    # Opções do menu, resp vai receber a resposta do usuário, qual opção ele escolheu:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    
    if resp == 1:
        # Opção de Exibir as pessoas do arquivo dados.txt
        ler_arquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa:
        cabecalho('NOVO CADASTRO')
        try:
            nome = input('Nome: ').lstrip().rstrip()
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não informar o nome. Então o nome é <desconhecido>.\033[m')
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # Opção de sair do sistema:
        cabecalho('SAINDO DO SISTEMA... ATÉ LOGO!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(0.5)
