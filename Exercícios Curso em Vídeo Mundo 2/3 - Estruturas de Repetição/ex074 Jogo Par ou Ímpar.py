from random import randint

qtde_vitorias = 0
jogar_de_novo = True
print("-="*20)
print("          JOGO PAR OU ÍMPAR")
print("-="*20)

# Enquanto o jogador quiser jogar de novo (Na primeira vez que ele executa o código, obviamente ele quer jogar de novo):
while jogar_de_novo == True:
    while True:
        jogador = input("Vamos jogar Par Ou Ímpar: Qual sua opção entre Par (P) ou Ímpar (I)? ").strip().lower()
        # Enquanto o jogador (Par ou Ímpar) for False (String vazia) ou a primeira letra que o usuário escrever (transformada em minúscula) não estiver dentro da lista de opções (pi):
        while not jogador or jogador[0] not in "pi":
            print("Opção inválida, por favor, digite novamente (P/I): ")
            jogador = input("Sua escolha: ").strip().lower()
        print("Vou escolher um número de 0 até 10...")
        # Filtra a escolha do jogador pegando só a primeira letra (que fica no índice 0) do que ele escreveu
        escolha_jogador = jogador[0]
        numero_jogador = int(input("Digite seu número: "))
        # Aleatoriza a escolha do computador, ele vai escolher um número de 0 até 10
        numero_comp = randint(0, 10)
        soma = numero_comp + numero_jogador
        # Se o jogador escolher "p":
        if escolha_jogador == "p":
            # Se a soma for par:
            if soma % 2 == 0:
                print(f"O número que eu pensei foi {numero_comp}, a soma é {soma}, que é PAR, perdi. Vamos jogar novamente!")
                qtde_vitorias += 1
                print(f"Vitórias até então: {qtde_vitorias}")
            # Se a soma for ímpar:
            elif soma % 2 == 1:
                print(f"O número que eu pensei foi {numero_comp}, a soma é {soma}, que é ÍMPAR, ganhei! Como você perdeu, acabou o jogo.")
                break
        # Se o jogador escolher "i":
        elif escolha_jogador == "i":
            # Se a soma for par:
            if soma % 2 == 0:
                print(f"O número que eu pensei foi {numero_comp}, a soma é {soma}, que é PAR, ganhei! Como você perdeu, acabou o jogo.")
                break
            # Se a soma for ímpar:
            elif soma % 2 == 1:
                print(f"O número que eu pensei foi {numero_comp}, a soma é {soma}, que é ÍMPAR, perdi. Vamos jogar novamente!")
                qtde_vitorias += 1
                print(f"Vitórias até então: {qtde_vitorias}")

# Quando o usuário perder, o computador pergunta se ele quer jogar de novo
    print(f"GAME OVER. Você ganhou {qtde_vitorias} vez(es). Se quiser, vamos jogar novamente!")
    jogar_de_novo = input("Deseja jogar de novo? (S/N): ").strip().lower()
    while not jogar_de_novo or jogar_de_novo[0] not in "sn":
        jogar_de_novo = input("Opção inválida, por favor, digite S ou N: ")
    # Se o usuário escolher que quer jogar de novo:
    if jogar_de_novo[0] == "s":
        # A variável jogar_de_novo vai receber a string "s", então convertemos ela para True:
        jogar_de_novo = True
        print("-="*50)
        # O loop volta ao começo, lá, ele faz a verificação se a variável jogar_de_novo é igual à True; como é igual, ele vai executar o código novamente até chegar na pergunta se ele quer jogar de novo ou não
    # Se o usuário escolher que não quer jogar de novo: 
    elif jogar_de_novo[0] == "n":
        print("-="*50)
        print("Fim do Software, obrigado!")
        # A variável jogar_de_novo recebe False, e assim o software sai do primeiro while loop e o software acaba:
        jogar_de_novo = False
