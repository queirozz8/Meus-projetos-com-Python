from time import sleep
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
opcao_usuario = 0
# While the user doesn't type 5, indicating that he wants to stop the software:
# Enquanto o usuário não digitar 5, indicando que ele quer parar o software:
while opcao_usuario != 5:
    # Always when the user types one of the options and the software does that, the software will return here, displaying the options again for the user:
    # Sempre quando o usuário digitar uma das opções e o software fizer aquilo, o software vai voltar aqui, exibindo as opções de novo para o usuário:
    opcao_usuario = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do Software
Digite sua opção: '''))
    # If the user chooses sum:
    # Se o usuário quiser somar:
    if opcao_usuario == 1:
        print(f"A soma de {n1} e {n2} é {n1 + n2}.\n")
        sleep(1)
        print("=-="*10)

    # If the user chooses multiplication:
    # Se o usuário escolher multiplicação:
    elif opcao_usuario == 2:
        print(f"A multiplicação de {n1} e {n2} é {n1 * n2}.\n")
        sleep(1)
        print("=-="*10)

    # If the user chooses the largest number between n1 and n2:
    # Se o usuário escolher o maior número entre n1 e n2:
    elif opcao_usuario == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        else:
            maior = n1
        print(f"O maior número entre {n1} e {n2} é {maior}.\n")
        sleep(1)
        print("=-="*10)

    # If the user chooses change the numbers:
    # Se o usuário escolher mudar os números:
    elif opcao_usuario == 4:
        n1 = float(input("Digite o novo valor: "))
        n2 = float(input("Digite o segundo novo valor: "))
        sleep(1)
        print("=-="*10)

    # If the user chooses exit the software:
    # Se o usuário escolher sair do software:
    elif opcao_usuario == 5:
        print("Saindo do Software...")
        sleep(1)
        print("=-="*10)

    # If the user chooses an invalid option:
    # Se o usuário escolher uma opção inválida:
    else: 
        print("Opção inválida, tente novamente!")
        sleep(1)
        print("=-="*10)
print("Fim do Software! Volte sempre!")
