# Era pra esse software ter mais cores, mas por causa de bugs, decidi colorir só algumas partes.
from time import sleep
# t vai ser a string que eu futuramente vou querer que essa função aborde:
def titulo(t):
    tam = len(t)
    print('~'*tam)
    # O título não vai ficar alinhado com outros títulos que não tenham códigos de cores neles iguais aos outros que eu coloquei, 
    # do fim do software PyHelp e o Sistema de Ajuda PyHelp, mas como eles são os únicos títulos, tudo bem fazer dessa forma:
    print(f'{t:^{tam + 9}}')
    # Retorna o texto à sua coloração normal:
    print('~'*tam)
    sleep(1)

def ajuda(com):
    titulo(f'\033[034mAcessando o manual/documentação do comando "{com.lstrip().rstrip()}":')
    # Usamos a função Built-In do Python chamada "Help()", que gera a documentação de cada função ou biblioteca:
    help(com)
    sleep(1)
    
# Programa Principal
while True:
    titulo('\033[032mSISTEMA DE AJUDA PyHELP\033[m')
    print('''Digite FIM/fim para sair. Se uma documentação é muito longa e quiser parar de ver, aperte a tecla "Q" do teclado. 
Aperte Enter para ir descendo na documentação, aperte Espaço para pular uma parte.''')
    comando = ''
    # Enquanto comando for uma string vazia:
    while not comando:
        comando = input('Função ou biblioteca (Se sua resposta for uma string vazia, a pergunta se repete)>')
    # Se o comando tornado em letras maiúsculas é igual à "FIM", saia do loop e termine o software:
    if comando.upper() in 'FIM':
        break
    ajuda(comando)
    
titulo(('\033[031mFIM DO SOFTWARE PyHELP!\033[m'))