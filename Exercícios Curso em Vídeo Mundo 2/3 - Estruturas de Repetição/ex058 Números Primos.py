num = int(input("Digite um número inteiro: "))
tot = 0
for numero_Atual in range(1, num + 1):
    # If the user's number is divisible by the current number:
    # Se o número do usuário for divisível pelo número atual:
    if num % numero_Atual == 0:
        # Color the number yellow:
        # Colore o número de amarelo:
        print("\033[33m", end=" ")
        # Total of numbers that were divisible receives +1:
        # O total de números que foram divisíveis recebe +1:
        tot += 1
    else:  
        # Color the number red:
        # Colore o número de vermelho:
        print("\033[31m", end=" ")
    print(f"{numero_Atual}", end=" ")
print("\33[m")
print(f"O número {num} é divisível por {tot} números anteriores à ele (Números que estão em amarelo são os divisíveis).")
# if the total of numbers that were divisible by the user's number is equal to 2:
# Se o total de números que foram divisíveis pelo número do usuário for igual à 2:
if tot == 2:
    print(f"Como {num} é divisível apenas 2 vezes (1 e ele mesmo), ele é PRIMO!")
else:
    print(f"Como {num} não é divisível 2 vezes, só por 1 e ele mesmo, ele NÃO É PRIMO!")
