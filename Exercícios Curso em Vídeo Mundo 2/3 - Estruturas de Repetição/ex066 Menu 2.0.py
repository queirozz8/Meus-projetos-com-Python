from time import sleep
# Previous configurations to the variables:
# Configurações prévias para as variáveis:
opcao = 0
soma = 0
maior = 0
maior_subtracao = 0
menor_subtracao = 0
quantos_numeros = int(input("Digite quantos números quer abordar (Mínimo 2) (Se quiser fazer subtrações e divisões, selecione 2 números): "))
# While the user doesn't type more than 1 number:
# Enquanto o usuário não digitar mais de 1 número:
while quantos_numeros < 2:
    print("Opção inválida, tente novamente com 2 números ou mais.")
    quantos_numeros = int(input("Digite quantos números quer abordar (Mínimo 2) (Se quiser fazer subtrações e divisões, selecione 2 números): "))
for numero_atual in range (1, quantos_numeros + 1):
    numero = float(input(f"Digite o {numero_atual}° número: "))
    # Sum
    # Soma
    soma += numero
    
    # Subtraction
    # Subtração
    if numero_atual == 1:
        subtracao_n1 = numero
    if numero_atual == 2:
        subtracao_n2 = numero
        if subtracao_n1 > subtracao_n2:
            maior_subtracao = subtracao_n1
            menor_subtracao = subtracao_n2
        elif subtracao_n1 < subtracao_n2:
            maior_subtracao = subtracao_n2
            menor_subtracao = subtracao_n1
        else:
            maior_subtracao = subtracao_n1
            menor_subtracao = subtracao_n2
    subtracao = maior_subtracao - menor_subtracao

    # Multiplication
    # Multiplicação
    if numero_atual == 1:
        multiplicacao = numero
    else:
        multiplicacao *= numero

    # Division
    # Divisão
    if numero_atual == 1:
        divisao_n1 = numero
        maior_divisao = divisao_n1
        menor_divisao = divisao_n1

    if numero_atual == 2:
        divisao_n2 = numero
        if divisao_n1 > divisao_n2:
            maior_divisao = divisao_n1
            menor_divisao = divisao_n2
        elif divisao_n1 < divisao_n2:
            maior_divisao = divisao_n2
            menor_divisao = divisao_n1
        else:
            maior_divisao = divisao_n1
            menor_divisao = divisao_n2
    divisao = maior_divisao / menor_divisao

    # Biggest and smallest number from the list of numbers
    # Maior e menor número da lista de números
    if numero > maior:
        maior = numero
    if numero_atual == 1:
        menor = numero
    if numero < menor:
        menor = numero

# While the user doesn't choose the 7 option (Exit the Software):
# Enquanto o usuário não escolher a opção 7 (Sair do Software):
while opcao != 7:
    # After that the user types the option he wants and the Sofware does that, the "while" is gonna to type ten times "=-=" and will go back here, showing the options again:
    # Depois que o usuário escrever a opção que ele quer fazer e o Software fizer o que ele queria, o "while" vai escrever 10 vezes "=-=" e vai voltar aqui, para mostrar de novo
    # as opções que o usuário pode escolher:
    opcao = int(input('''
[1] SOMA
[2] SUBTRAÇÃO (Só com 2 números)
[3] MULTIPLICAÇÃO
[4] DIVISÃO (Só com 2 números)
[5] MAIOR NÚMERO E MENOR NÚMERO
[6] SUBSTITUIR OS NÚMEROS
[7] SAIR DO SOFTWARE
Digite sua escolha: '''))

    # If the choosen option is SUM:
    # Se a opção escolhida for SOMA:
    if opcao == 1:
        print(f"A SOMA dos números dá {soma}.")
        sleep(1)
        print("=-="*10)

    # If the choosen option is SUBTRACTION:
    # Se a opção escolhida for SUBTRAÇÃO:
    elif opcao == 2:
        # If the subtraction numbers is 2 numbers:
        # Se os números para subtrair forem 2 números:
        if quantos_numeros == 2:
            print(f"A SUBTRAÇÃO dos números dá {subtracao}.")
            sleep(1)
            print("=-="*10)
        # if the subtraction numbers is above 2 numbers:
        # Se a os números para subtrair forem 2 números: 
        else:
            print("A subtração só é feita com 2 números, por favor, tente novamente apertando 6 e trocando para 2 números.")
        sleep(1)
        print("=-="*10)

    # If the choosen option is MULTIPLICATION?
    # Se a opção escolhida for MULTIPLICAÇÃO:
    elif opcao == 3:
        print(f"A MULTIPLICAÇÃO dos números dá {multiplicacao:.3f}.")
        sleep(1)
        print("=-="*10)
    
    # If the choosen option is DIVISION
    # Se a opção escolhida for DIVISÃO
    elif opcao == 4:
        if quantos_numeros == 2:
            print(f"A DIVISÃO dos números dá {divisao:.3f}.")
            sleep(1)
            print("=-="*10)
        else:
            print("A divisão só é feita com 2 números, por favor, tente novamente apertando 6 e trocando para 2 números.")
            sleep(1)
            print("=-="*10)
        
    # If the chossen option is to know the biggest and smallest numbers:
    # Se a opção escolhida for saber qual é o maior e o menor número:
    elif opcao == 5:
        print(f"O MAIOR número entre os {quantos_numeros} números escritos é {maior}, o MENOR número é {menor}.")
        sleep(1)
        print("=-="*10)

    # If the user chooses to change the numbers:
    # Se o usuário escolher trocar os números:
    elif opcao == 6:
        quantos_numeros = int(input("Digite quantos números quer abordar (Mínimo 2) (Se quiser fazer subtrações e divisões, selecione 2 números): "))
        # While the user doesn't type more than 1 number:
        # Enquanto o usuário não digitar mais de 1 número:
        while quantos_numeros < 2:
            print("Opção inválida, tente novamente com 2 números ou mais.")
            quantos_numeros = int(input("Digite quantos números quer abordar (Mínimo 2) (Se quiser fazer subtrações e divisões, selecione 2 números): "))
        
        # Redo the variable configuration:
        # Refaz a configuração das variáveis:
        for numero_atual in range (1, quantos_numeros + 1):
            numero = float(input(f"Digite o {numero_atual}° novo número: "))

            # Sum
            # Soma
            soma += numero

            # Subtraction
            # Subtração
            if numero_atual == 1:
                subtracao_n1 = numero

            if numero_atual == 2:
                subtracao_n2 = numero
                if subtracao_n1 > subtracao_n2:
                    maior_subtracao = subtracao_n1
                    menor_subtracao = subtracao_n2
                elif subtracao_n1 < subtracao_n2:
                    maior_subtracao = subtracao_n2
                    menor_subtracao = subtracao_n1
                else:
                    maior_subtracao = subtracao_n1
                    menor_subtracao = subtracao_n2
            subtracao = maior_subtracao - menor_subtracao

            # Multiplication
            # Multiplicação
            if numero_atual == 1:
                multiplicacao = numero
            else:
                multiplicacao *= numero


            # Division
            # Divisão
            if numero_atual == 1:
                divisao_n1 = numero
                maior_divisao = divisao_n1
                menor_divisao = divisao_n1

            if numero_atual == 2:
                divisao_n2 = numero
                if divisao_n1 > divisao_n2:
                    maior_divisao = divisao_n1
                    menor_divisao = divisao_n2
                elif divisao_n1 < divisao_n2:
                    maior_divisao = divisao_n2
                    menor_divisao = divisao_n1
                else:
                    maior_divisao = divisao_n1
                    menor_divisao = divisao_n2
            divisao = maior_divisao / menor_divisao


            # Biggest and smallest number from the number's list
            # Maior e menor número da lista de números
            if numero > maior:
                maior = numero
            if numero_atual == 1:
                menor = numero
            if numero < menor:
                menor = numero
    
    # If the user chooses exit from the Software:
    # Se o usuário escolher sair do Software:
    elif opcao == 7:
        print("Saindo...")
    
    # If the user chooses an invalid option:
    # Se o usuário escolher uma opção inválida:
    else:
        print("Opção inválida, por favor, tente novamente.")
print("Fim do Software! Obrigado e volte sempre!")
