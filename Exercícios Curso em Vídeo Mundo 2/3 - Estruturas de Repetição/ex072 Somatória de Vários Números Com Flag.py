print("SOMADOR DE NÚMEROS INFINITAMENTE (DIGITE 999 PARA PARAR DE SOMAR)")
qtde = soma = 0
while True:
    num = int(input("Digite um número (999 para parar): "))
    # Se o número digitado pelo usuário for 999:
    if num == 999:
        # Interrompa o While Loop
        break
    # Se o número não for 999, a quantidade de números digitados (qtde) recebe +1, e a soma de todos os números recebe o número atual:
    qtde += 1
    soma += num
print("-="*30)
print(f"A soma dos {qtde} números digitados é {soma}.")
