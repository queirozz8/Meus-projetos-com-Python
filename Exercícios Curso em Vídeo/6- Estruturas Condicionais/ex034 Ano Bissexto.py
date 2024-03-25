from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
# Se o usuário colocar 0 na resposta:
if ano == 0:
    '''The computer will show if the CURRENT year that your machine it's running it's a leap year or not
    O computador vai te mostrar se o ano ATUAL da sua máquina é bissexto ou não'''
    ano = date.today().year
# Se o usuário não escrever 0: 

# If the year that the user entered it's divisible by 4 AND NOT divisible by 100, OR if the year it's divisible by 400: Mean that the year entered it's a LEAP YEAR
# Se o ano que o usuário escreveu for divisível por 4 E NÃO for divisível por 100, OU se o ano for divisível por 400: Quer dizer que esse ano é um ano BISSEXTO
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else: # If it's not all that things, the year it's not leap |  Se não for todas essas coisas quer dizer que o ano não é bissexto
    print(f"O ano {ano} NÃO é BISSEXTO")
