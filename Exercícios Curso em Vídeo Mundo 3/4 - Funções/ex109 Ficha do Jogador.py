# Criei a função ficha, que representa a ficha do jogador. Por padrão, o nome fica como '<Desconhecido>', e a quantidade de gols fica com 0:
def ficha(jog='<Desconhecido>', gol=0):
    print('-='*30)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato de futebol.')

# Programa Principal
print('OBS: Se o usuário não informar um nome para o jogador, ele fica com o nome de "<Desconhecido>". Se o usuário não digitar a quantidade de gols, automaticamente fica com 0.')
print('-='*30)
n = input('Nome do jogador: ').lstrip().rstrip()
# g por enquanto é uma string, porque se fosse um int, o Python não deixaria o usuário deixar uma resposta vazia como input:
g = input('Gols: ')
# Se a string que o usuário digitar for um caractere numérico:
if g.isnumeric():
    # Então transformamos a string do número digitado em um número mesmo:
    g = int(g)
else:
    # Caso não for um número, ele fica automaticamente com 0:
    g = 0

# Se o nome do jogador com o strip for uma string vazia, então chamamos a função, mas só passando o parâmetro do gol, que só pode ser 0 ou o número que o usuário digitou:
if n.strip() == '':
    ficha(gol=g)
# Se o nome for uma string com algo dentro, então chamamos a função, agora com os parâmetros de nome e gol (n e g), o que vai resultar no resultado padrão:
else:
    ficha(n, g)