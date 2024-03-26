salario = float(input("Qual é o salário do funcionário? R$"))
# If the salary it's lower or equal to 1250 reais (Brazil's money):
# Se o salário for menor ou igual a 1250 reais:
if salario <= 1250:
    # The new salary of the employee will get an extra amount of 15%
    # O novo salário do funcionário vai receber um aumento de 15%
    novo = salario + (salario * 15 / 100)
else:
    # The new salary of the employee will get an extra amount of 10%
    # O novo salário do funcionário vai receber um aumento de 10%
    novo = salario + (salario * 10 / 100)
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.")
