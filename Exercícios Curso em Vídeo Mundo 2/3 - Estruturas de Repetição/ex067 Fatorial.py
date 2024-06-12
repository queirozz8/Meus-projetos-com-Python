# I'm going to do in 3 ways
# Eu vou fazer de 3 formas
from math import factorial
numero = int(input("Digite um número para calcular seu fatorial: "))
fatorial_jeito_2_e_3 = 1
contador_jeito_2 = numero
fatorial_jeito_1 = factorial(numero)

# Way 1
# Jeito 1
'''print(f"O fatorial de {numero} = {fatorial_jeito_1}.")'''

# Way 2
# Jeito 2
print(f"Calculando {numero}! ...")
# While the counter is not 0:
# Enquanto o contador não chegar no 0:
while contador_jeito_2 > 0:
    # It prints the number that the counter is, that is, the number and every previous numbers:
    # Escreve o número que o contador está, isso é, o número e em seguida todos os antecedentes dele:
    print(f"{contador_jeito_2}", end="")
    # If the counter isn't 0, it will print "x" for print the next numbers that the 'contador_jeito_2' is gonna to pass until it arrives at 0:
    # Se o contador não estiver no 0, ele vai escrever "x" para escrever os próximos números que o contador_jeito_2 vai passar até chegar no 0:
    if contador_jeito_2 > 1:
        print(" x ", end="")
    # If the counter is 0, it will print "=" for print the factorial at the final:
    # Se o contador estiver no 0, ele vai escrever o "=" para mostrar o fatorial no final:
    else:
        print(" = ", end="")
    # 'Fatorial' is going to receive the 'numero' (number) and every previous numbers multiplicated:
    # Fatorial vai receber o 'numero' e todos os seus antecedentes multiplicados:
    fatorial_jeito_2_e_3 *= contador_jeito_2
    # When 'while' has done everything it had to do, the counter increments by one, and the loop restarts until the counter reaches 0:
    # Quando o 'while' tiver feito tudo que tinha para fazer, o contador desce um, e o loop reinicia até o contador chegar no 0: 
    contador_jeito_2 -= 1
# When the counter arrives at 0, the Software exits from the while loop, and it's gonna to print the factorial of the number at the final, after "=":
# Quando o contador chegar a 0, o Software vai sair do 'while', e vai escrever o fatorial do número no final, depois do "=":
print(fatorial_jeito_2_e_3)


# Way 3
# Jeito 3
# For the third way, I take the number 5
# Para o jeito 3, eu peguei o número 5
'''print(f"Calculando {numero}! ...")
for cada_numero in range(5, 0, -1):
    # It prints the number that the counter is, that is, the number and every previous numbers:
    # Escreve o número que o contador está, isso é, o número e em seguida todos os antecedentes dele:
    print(f"{cada_numero}", end="")
    # If the counter isn't 0, it will print "x" for print the next numbers that the 'contador_jeito_2' is gonna to pass until it arrives at 0:
    # Se o contador não estiver no 0, ele vai escrever "x" para escrever os próximos números que o contador_jeito_2 vai passar até chegar no 0:
    if cada_numero > 1:
        print(" x ", end="")
    # If the counter is 0, it will print "=" for print the factorial at the final:
    # Se o contador estiver no 0, ele vai escrever o "=" para mostrar o fatorial no final:
    else:
        print(" = ", end="")
    # 'Fatorial' is going to receive 'cada_numero' (each number) and every previous numbers multiplicated:
    # Fatorial vai receber o 'cada_numero' e todos os seus antecedentes multiplicados:
    fatorial_jeito_2_e_3 *= cada_numero
# When the counter arrives at 0, the Software exits from the for loop, and it's gonna to print the factorial of the number at the final, after "=":
# Quando o contador chegar a 0, o Software vai sair do for, e vai escrever o fatorial do número no final, depois do "=":
print(fatorial_jeito_2_e_3)'''
