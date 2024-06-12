print("Gerador de PROGRESSÃO ARITMÉTICA")
print("-="*20)
termo = int(input("Digite o primeiro termo da sua Progressão Aritmética: "))
razao = int(input("Digite a razão da sua Progressão Aritmética: "))
# 'contador' (Counter) will receive the function of "How many times we are gonna print the numbers on the Terminal"
# Contador vai ser quem define quantas vezes vamos mostrar os números no Terminal:
contador = 1
# Total will count every numbers that the user typed:
# Total vai contar todos os números que o usuário digitou:
total = 0
# 'Mais' (more) will be how many numbers the user wants to show more, by defaut it starts with 10, and if the user wants more numbers, the total of numbers that the user wanted to add go to 'total'
# Mais vai ser quantos números o usuário quer mostrar à mais, por padrão ele começa com 10, e se caso o usuário for querer mostrar mais números, o total de números que o usuário quis adicionar vai ir para 'total':
mais = 10
# While user doesn't type that he wants to stop from printing the numbers:
# Enquanto o usuário não dizer que quer parar de mostrar os números:
while mais != 0:
    # The total of numbers receive 'mais', so the total will receive 10 initially
    # O total de números recebe 'mais', então o total vai receber 10 inicialmente
    total += mais
    # While 'contador' is lower or equal to total (initially 10), the Software prints the number 'termo' (Term):
    # Enquanto o contador for menor ou igual ao total (inicialmente 10), o Software mostra o número 'termo':
    while contador <= total:
        # Prints the number 'termo' added to the 'razao' (difference number) that the user wanted to put. So if the 'razao' is 2 and 'termo' is 0, will be "0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6, 6 + 2 = 8" and so on
        # Mostra o número 'termo' somado com a razão que o usuário quis colocar. Então se a razão for 2 e o primeiro termo for 0, vai ser "0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6, 6 + 2 = 8" e assim por diante.
        print(f"{termo} → ", end="")
        termo += razao
        # Counter will receive +1, until he gets and surpass 'total': 
        # Contador vai receber +1, até chegar e ultrapassar o total:
        contador += 1
    print("PAUSA.")
    # 'mais' will ask the user if he wants to show more numbers, so if the user says that he wants to show more 5 numbers, 'total' will receive 10 + 5, and the counter will have to show more 5 numbers to reach
    # 'total', consequently the variable 'termo' will print more 5 numbers with the 'razao' (Difference number) that the user asked for:
    # 'mais' vai perguntar se o usuário quer mostrar mais números, então se o usuário disser que quer mostrar mais 5 números, total vai receber 10 + 5, e o contador vai ter que mostrar mais 5 números para chegar
    # no 'total', consequentemente a variável 'termo' vai mostrar mais 5 números com a razão que o usuário pediu:
    mais = int(input("Digite quantos números deseja mostrar à mais (Caso não queira digitar mais número nenhum, digite 0): "))
# At final, when te user type 0, the Software skip a line in the start and final, and says the total of numbers that the user asked for showing, that is, show the variable 'total':
# No final, quando o usuário escrever 0, o Software pula uma linha no começo e no final, e diz o total de números que o usuário pediu para mostrar, isso é, mostra a variável 'total':
print(f"\nFIM da sua PROGRESSÃO ARITMÉTICA, ao todo, foram {total} números mostrados.\n")
