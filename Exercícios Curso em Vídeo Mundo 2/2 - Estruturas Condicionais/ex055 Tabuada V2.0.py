print("      TABUADA")
print("-"*20)
tabuada = int(input("Digite um NÚMERO INTEIRO para fazer-mos sua TABUADA: "))
print(f"A tabuada do número {tabuada} é: \n")
# For every number (1, 10):
# Para cada número (1, 10):
for numero in range(1, 11):
    # Print the chosen number for the multiplication table (tabuada) * the numbers (1, 10) (numero)
    # Escreva o número escolhido para a tabuada (tabuada) * os números de 1 até 10 da tabuada (numero)
    print(f"{tabuada} x {numero} = {tabuada * numero}")
