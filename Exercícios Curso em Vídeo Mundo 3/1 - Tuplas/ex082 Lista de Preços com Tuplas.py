produtos = ("Lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)
print("-="*20)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-="*20)
# Todos os nomes de produtos ficam num índice par, todos os preços ficam num índice ímpar. Para cada posição da tupla produtos (O tamanho dela é pego com o len):
for pos in range(len(produtos)):
    # Se a posição for par:
    if pos % 2 == 0:
        # Mostre o nome do produto (Que está na posição pos) alinhado à esquerda, e com "." até 30 caracteres:
        print(f"{produtos[pos]:.<30}", end="")
    # Se a posição for ímpar:
    else:
        # Mostre o preço do produto (Que está na posição pos) formatado com 2 espaços depois da vírgula:
        print(f" R$ {produtos[pos]:.2f}")
print("-="*20)

# Outra forma de se fazer esse software, não fiz assim pois o enunciado pediu que fosse com 1 tupla só, mas podemos fazer com mais tuplas:
'''produtos = ("Lápis",
            "Borracha",
            "Caderno",
            "Estojo",
            "Transferidor",
            "Compasso",
            "Mochila",
            "Canetas",
            "Livro")

precos = (1.75,
          2,
          15.90,
          25,
          4.20,
          9.99,
          120.32,
          22.30,
          34.90)
print("-="*20)
print(f"{"LISTAGEM DE PREÇOS":.^40}")
print("-="*20)

for i in range(len(produtos)):
    print(f"{produtos[i]:.<30}", end="")
    print(f" R$ {precos[i]:.2f}")
print("-="*20)'''
