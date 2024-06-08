from datetime import date
oi = "ola mundo"
print(oi [2:])
print("    CLASSIFICADOR DE ATLETAS")
print("-"*30)
print('''CATEGORIAS:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima disso: MASTER''')
ano_Nasc = int(input("Digite o ano de nascimento do atleta: "))
# Get the current year:
# Pega o ano atual:
ano_Atual = date.today().year
idade = ano_Atual - ano_Nasc
if idade <= 9:
    print(f"O atleta é um atleta MIRIM, pois tem {idade} anos.")
elif idade <= 14: 
    print(f"O atleta é um atleta INFANTIL, pois tem {idade} anos.")
elif idade <= 19:
    print(f"O atleta é um atleta JUNIOR, pois tem {idade} anos.")
elif idade <=25:
    print(f"O atleta é um atleta SÊNIOR, pois tem {idade} anos.")
else:
    print(f"O atleta é um atleta MASTER, pois tem {idade} anos e tem mais de 25 anos.")
