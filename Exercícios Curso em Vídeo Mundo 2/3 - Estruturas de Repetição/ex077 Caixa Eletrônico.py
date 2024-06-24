from time import sleep
print("-"*30)
print(f"{"BANCO RICK":^30}")
print("-"*30)
print("CAIXA ELETRÔNICO FEITO POR RICK.")
print("CÉDULAS DISPONÍVEIS: 200 reais, 100 reais, 50 reais, 20 reais, 10 reais, 5 reais, 2 reais, 1 real")
valor = int(input("Qual valor (Inteiro) você quer SACAR? R$"))
# valor_original é só o valor inicial que o usuário pediu para sacar, ela serve para mostrar o valor total do saque para o usuário no final:
valor_original = valor
# ced começa com a maior cédula, nesse caso, 200:
ced = 200
# tot_ced começa com 0, vai ser o contador de quantas cédulas de tal valor o Caixa Eletrônico precisa dar para o usuário
tot_ced = 0
print("-="*30)

while True:
    # Se o valor for maior ou igual à cédula atual:
    if valor >= ced:
        # O valor total é descontado da cédula atual:
        valor -= ced
        # O contador de cédulas para cada cédula recebe +1
        tot_ced += 1
    else:
        # O Software só vai mostrar a cédula caso a quantidade dela seja mais que 0:
        if tot_ced > 0:
            sleep(0.3)
            print(f"{tot_ced} cédula(s) de R${ced}.")

        # Se o valor total for menor que a cédula atual e a cédula for 200:
        if ced == 200:
            # Então a cédula vira 100, e o Software vai tentar descontar do valor com ela:
            ced = 100
        # Caso não dê, isso é, se o valor total for menor que a cédula atual e a cédula for 100:
        elif ced == 100:
            # Então a cédula vira 50, e o Software vai tentar descontar do valor com ela:
            ced = 50
        # E assim por diante em todas as cédulas:
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        # Após uma cédula ser trocada por outra, o tot_ced reinicia, pois agora estamos contando outra cédula:
        tot_ced = 0
        
        # Quando o valor total chegar em 0:
        if valor == 0:
            sleep(1)
            print("-="*30)
            # O Software termina
            print(f"FIM DO SAQUE DE R${valor_original}, VOLTE SEMPRE!")
            break
