from random import randint
# Sorteia 5 números de 0 até 10 e guarda eles em uma tupla
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Eu sorteei os valores: {num}")
# max retorna o maior valor dentro de uma estrutura de dados:
print(f"O MAIOR valor sorteado foi {max(num)}.")
# min retorna o menor valor dentro de uma estrutura de dados:
print(f"O MENOR valor sorteado foi {min(num)}.")
