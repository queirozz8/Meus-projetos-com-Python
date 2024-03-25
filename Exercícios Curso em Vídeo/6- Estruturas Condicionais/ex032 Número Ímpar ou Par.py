numero = int(input("Digite um número: "))
# If the remainder of a number divided by 2 is equal to 0, it is a even number
# Se o resto de um número dividido por 2 é igual a 0, ele é par
resultado = numero % 2
if resultado == 0:
    print(f"O número {numero} é par")
else: # if not, it is a odd number | Se não, ele é ímpar
    print(f"O número {numero} é ímpar")
