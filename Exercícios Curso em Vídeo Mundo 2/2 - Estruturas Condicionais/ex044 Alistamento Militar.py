from datetime import date
print("-"*20)
print("     ALISTAMENTO MILITAR OBRIGATÓRIO")
print("-"*20)

sexo = str(input("Qual seu sexo? (H/M): ")).strip() .lower()
# If the gender is male:
# Se o sexo for masculino:
if sexo == "h":
    ano_Nasc = int(input("Digite o seu ano de NASCIMENTO (Sem o dia/mês): "))
    ano_Atual = date.today().year
    idade = ano_Atual - ano_Nasc
    print(f"Quem nasceu em {ano_Nasc} tem {idade} anos em {ano_Atual}.")
    if idade < 18:
        saldo = 18 - idade
        print(f"Você ainda tem {idade} anos, ainda não precisa se alistar! falta(m) {saldo} ano(s).")
        ano = ano_Atual + saldo
        print(f"Seu alistamento será em {ano}.")
    elif idade == 18:
        print(f"Você tem {18} anos, chegou a hora de você se alistar para o exército brasileiro!")
    elif idade > 18:
        saldo = idade - 18
        ano = ano_Atual - saldo
        print(f"Você já passou dos 18, não precisa mais se alistar para o exercito brasileiro. Deveria ter se alistado em {saldo} ano(s) atrás.")
        print(f"Seu alistamento foi em {ano}.")
# If the gender is female:
# Se o sexo for feminino:
else:
    print("Você é mulher e não precisa se alistar para o Alistamento Militar Obrigatório.")
