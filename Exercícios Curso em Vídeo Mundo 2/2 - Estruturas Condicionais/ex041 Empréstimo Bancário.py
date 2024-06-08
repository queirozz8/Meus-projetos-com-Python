print("       BANCO")
print("-"*20)
valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Digite em quantos anos você vai pagar a casa: "))
# Ex: If the user wants to finantiate in 10 years, 10 * 12 = 120, 120 / value
# Ex: Se o usuário quiser financiar em 10 anos, 10 * 12 = 120, 120 / valor
prestacoes_Mes = valor / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R${valor:.2f} em {anos}, a prestação será de {prestacoes_Mes:.2f}")
if prestacoes_Mes <= minimo:
    print("Você consegue pagar essa prestação pois ela não excede 30% do seu salário, EMPRÉSTIMO CONCEDIDO.")
else:
    print("EMPRÉSTIMO NEGADO, pois o valor da casa supera 30% do seu salário.")
