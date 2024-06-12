maior = 0
menor = 0
for pessoa in range(1, 6):
    kg = float(input(f"Digite o peso da {pessoa}° pessoa: "))
    # When the user digits the first person, both the largest and smallest number receives the first value:
    # Quando o usuário digitar a primeira pessoa, tanto o maior número quanto o menor recebem o primeiro valor:
    if pessoa == 1:
        maior = kg
        menor = kg
    else:
        # If the current typed weight is more than the old weight saved in the variable "maior", "maior" becomes that value:
        # Se o peso atual digitado for maior do que o peso anterior guardado na variável "maior", "maior" passa a ser esse valor:
        if kg > maior:
            maior = kg
        # If the current typed weight is less than the old weight saved in the variable "menor", "menor" becomes that value:
        # Se o peso atual digitado for menor do que o peso anterior guardado na variável "menor", "menor" passa a ser esse valor:
        elif kg < menor:
            menor = kg
print(f"O MAIOR peso lido foi de {maior}Kg.")
print(f"O MENOR peso lido foi de {menor}Kg.")
