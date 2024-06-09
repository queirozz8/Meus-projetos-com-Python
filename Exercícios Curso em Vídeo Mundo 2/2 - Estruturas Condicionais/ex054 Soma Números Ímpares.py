soma = 0
cont = 0
# Verify if the current number is odd:
# Verifica se o número atual é ímpar:
for numero_atual in range(1, 501, 2):
    # Verify if the number is divisible by 3:
    # Verifica se o número é divisível por 3:
    if numero_atual % 3 == 0:
        soma += numero_atual
        cont += 1
print(f"A soma de {cont} os valores solicitados é {soma}")
