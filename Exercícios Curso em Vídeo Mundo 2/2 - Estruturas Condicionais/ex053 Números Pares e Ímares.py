print("MOSTRADOR DE NÚMEROS PARES/ÍMPARES DE UMA SEQUÊNCIA DE NÚMEROS")
print("-"*67)
par_ou_impar = int(input('''
[1] Para PAR
[2] PARA ÍMPAR
Qual sua escolha? (1/2): '''))
# If the user chooses even:
# Se o usuário escolher par:
if par_ou_impar == 1:    
    numero_escolhido = int(input("Digite até quanto você quer que eu conte (Só mostrarei os números PARES de 1 até o número escolhido) (número inteiro): "))
    print(f"Os números PARES de 1 até {numero_escolhido} são:")
    # For every number between 2 and the chosen number:
    # Para cada número entre 2 e o número escolhido:
    for numero_atual in range(2, numero_escolhido+1, 2):
        # If the current number is even:
        # Se o número atual for par:
        if numero_atual % 2 == 0:
            print(numero_atual)
        # If the number isn't even, the software doesn't exibes it
        # Se o número não for par, o software não mostra ele

# If the user chooses odd:
# Se o usuário escolher ímpar:
elif par_ou_impar == 2:
    numero_escolhido = int(input("Digite até quanto você quer que eu conte (Só mostrarei os números ÍMPARES de 1 até o número escolhido) (número inteiro): "))
    # If the chosen number is less than 1:
    # Se o número escolhido for menor que 1:
    if numero_escolhido < 1:
        print("Por favor, tente novamente, o mínimo que você pode colocar para números ÍMPARES é 1, não digite abaixo disso.")
    else:
        print(f"Os números ÍMPARES de 1 até {numero_escolhido} são:")
    # For every number between 1 and the chosen number:
    # Para cada número entre 1 e o número escolhido:
    for numero_atual in range(1, numero_escolhido+2):
        # If the current number is odd:
        # Se o número atual for ímpar:
        if numero_atual % 2 == 1:
            print(numero_atual)
        # If the number is not odd, the software doesn't exibes it
        # Se o numero não for ímpar, o software não exibe ele
# If the user chooses an invalid option:
# Se o usuário escolher uma opção inválida:
else:
    print("Opção inválida, tente novamente entre as opções PAR (1) ou ÍMPAR (2).")
