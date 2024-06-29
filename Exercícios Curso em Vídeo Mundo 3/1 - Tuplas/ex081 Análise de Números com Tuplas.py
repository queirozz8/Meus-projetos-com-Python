# Colocando todos os números digitados pelo usuário dentro da tupla num:
num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))
print("-"*30)

print(f"\nVocê DIGITOU OS VALORES: {num}")
print("-"*30)

# count(9) conta todos os valores 9 que estão dentro daquela estrutura de dados:
print(f"\nO valor 9 APARECEU {num.count(9)} vez(es).")
print("-"*30)

# Se houver um número 3 em algum lugar da tupla:
if 3 in num:
    # index(3)+1 mostra o índice da primeira ocorrência daquele elemento, +1 é para facilitar a legibilidade, pois se não, os índices iriam começar em 0:
    print(f"\nO valor 3 APARECEU PELA PRIMEIRA VEZ na {num.index(3)+1}° posição.")
else:
    print("\nO valor 3 NÃO FOI DIGITADO em nenhuma posição.")
print("-"*30)


print("\nOs valores PARES digitados foi(foram): ", end="")
qtde_pares = 0
# Para cada número (Possivelmente par) dentro da tupla num:
for numeros_pares in num:
    # Se o número atual for par:
    if numeros_pares % 2 == 0:
        # Então a quantidade de pares recebe +1:
        qtde_pares += 1
print(f"{qtde_pares} valor(es). ", end="") 
if qtde_pares > 0:
    print(f"Números pares digitados: ", end="")
    # Para cada número (Possivelmente par) dentro da tupla num:
    for numeros_pares in num:
        # Se o número for par:
        if numeros_pares % 2 == 0:
            # Mostre o número par:
            print(f"{numeros_pares} ", end="")
    # Pula uma linha:
    print()
# Mas se a quantidade de números pares for igual à 0, quer dizer que nenhum valor par foi digitado, então mostre isso na tela:
elif qtde_pares == 0:
    print("NENHUM VALOR PAR foi digitado.")
print("-"*30)


print("\nOs valores ÍMPARES digitados foi(foram): ", end= "")
qtde_impares = 0
# Para cada número (Possivelmente ímpar) dentro da tupla num:
for numeros_impares in num:
    # Se o número for ímpar:
    if numeros_impares % 2 == 1:
        # Então a quantidade de ímpares recebe +1:
        qtde_impares += 1
print(f"{qtde_impares} valor(es). ", end="")
if qtde_impares > 0:
    print(f"Números ímpares digitados: ", end="")
    # Para cada número (possivelmente ímpar) dentro da tupla num:
    for numeros_impares in num:
        # Se o número for ímpar:
        if numeros_impares % 2 == 1:
            # Mostre o número ímpar:
            print(f"{numeros_impares} ", end="")
    # Pula uma linha:
    print()
# Mas se a quantidade de números ímpares for igual à 0, quer dizer que nenhum valor par foi digitado, então mostre isso na tela: 
elif qtde_impares == 0:
    print("NENHUM VALOR ÍMPAR foi digitado.")
print("-"*30)
