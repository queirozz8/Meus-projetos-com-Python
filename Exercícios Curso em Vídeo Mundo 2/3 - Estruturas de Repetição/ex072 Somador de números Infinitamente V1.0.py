# The response previously starts with "s", because the user doesn't typed the answer yet, so let's suppose that he wants. Anyway, the response of him will maybe change accordingly with his response
# A resposta previamente começa com "s", pois o usuário não digitou a resposta ainda, então vamos supor que ele quer. De qualquer forma, a resposta dele vai mudar de acordo com o que ele responder
resp = "s"
# Sum, amount, lower, greater and medium receive 0:
# Soma, quantidade, menor, maior e media recebem 0:
soma = quant = menor = maior = media = 0

# While the answer is yes (Both uppercase and lowercase):
# Enquanto a reposta for sim (Tanto maiúsculo quanto minúsculo):
while resp in "Ss":
    num = int(input("Digite um número: "))
    # 'soma' will receive the number and sum it with the previous value that the variable has
    # Soma vai receber o número, e somar ele com o valor prévio que ele já tinha
    soma += num
    # 'quant' (amount) will receive +1, because another number has added by the user:
    # Quantidade vai receber +1, pois mais um número foi falado pelo usuário:
    quant += 1
    # If the amount is 1:
    # Se a quantidade for igual a 1:
    if quant == 1:
        # Maior e menor vai receber o número, pois não tem outro número para se comparar com o número que foi falado:
        maior = menor = num
    # Se o número digitado atualmente for maior do que o maior número de antes:
    if num > maior:
        # A variável maior vai receber o número atual, pois ele é maior que o número antigo armazenado nessa variável:
        maior = num
    # If current typed number it's lower than the previous number:
    # Se o número digitado atualmente for menor do que o menor, número de antes: 
    if num < menor:
        # The variable 'menor' (lower) will receive the current number, because it's lower than the older number stored in this variable:
        # A variável menor vai receber o número atual, pois ele é menor que o número antigo armazenado nessa variável:
        menor = num
    resp = str(input("Deseja continuar? (S/N): ")).lower().strip()
# 'media' (Average) will receive the result of the sum of all numbers divided by the amount:
# 'media' vai receber o resultado da soma de todos os números dividido pela quantidade:
media = soma / quant
print(f"Você digitou {quant} número(s), a SOMA dele(s) é {soma}, a MÉDIA dele(s) é {media}.")
print(f"O MAIOR número digitado foi {maior}, o MENOR número digitado foi {menor}")
