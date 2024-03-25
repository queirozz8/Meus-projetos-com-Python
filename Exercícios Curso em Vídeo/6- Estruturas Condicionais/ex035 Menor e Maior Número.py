a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Checking who it's smaller
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Checking who it's bigger
# Verificando quem é maior
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"Entre os números {a}, {b}, {c}:")
print(f"O MENOR valor digitado foi {menor}")
print(f"O MAIOR valor digitado foi {maior}")
