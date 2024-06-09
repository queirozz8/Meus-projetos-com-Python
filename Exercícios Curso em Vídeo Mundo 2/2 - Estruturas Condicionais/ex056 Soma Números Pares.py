# "soma" = sum of all numbers at the final, if the current number (numero_atual) is even, it's acrescentated in the sum of all numbers
# "cont" = stores every even number that the user gave
# soma = soma de todos os números do final, se um número for par, ele é acrescentado na soma de todos os números
# cont = guarda todos os números pares que foram digitados pelo usuário
soma = 0
cont = 0
for numero_atual in range(1, 7):
    numero = int(input(f"Digite o {numero_atual}° número: "))
    # If the number is even:
    # Se o número é par:
    if numero % 2 == 0:
        # Sum will add the number the user just entered into itself, with all other even numbers the user entered before the current number
        # Soma vai acrescentar o número que o usuário acabou de digitar dentro dela mesma, com todos os outros números pares que o usuário digitou antes do número atual
        soma += numero
        cont += 1
print(f"Você digitou {cont} número(s) PAR(ES) e a soma é {soma}.")
