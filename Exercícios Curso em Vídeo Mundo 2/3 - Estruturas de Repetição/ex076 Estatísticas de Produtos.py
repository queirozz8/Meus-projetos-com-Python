print("-"*30)
print("      LOJA SUPER BARATÃO")
print("-"*30)
valor_tot = mais_1000 = barato = cont = produtos_cadastrados = caro = 0
while True:
    cont += 1
    produto = input("Qual é o nome do produto? ").lstrip().rstrip()
    preco = float(input("Qual é o preço do produto? R$"))
    
    # O valor total das compras vai receber o preço do produto atual somado com o valor antigo do valor_tot:
    valor_tot += preco
    
    # produtos_cadastrados recebe +1 à cada produto que o usuário cadastrar:
    produtos_cadastrados += 1
    
    # Se o preço do produto atual for maior que R$1000:
    if preco > 1000:
        mais_1000 += 1

    # Se o preço for maior que o preço antigo alocado na variável caro:
    if preco > caro:
        # Então caro recebe o preço do produto atual
        caro = preco
        # E o nome_caro recebe o nome do produto atual
        nome_caro = produto

    # Se o produto digitado for o primeiro produto, ou se o produto for mais barato que o produto mais barato anterior (Alocado no barato):
    if cont == 1 or preco < barato:
        # Então barato recebe o preco do produto atual
        barato = preco
        # E o nome_barato recebe o nome do produto atual
        nome_barato = produto

    print("-"*20, "\n")
    print("Produto cadastrado.")
    continuar = input("Deseja continuar cadastrando mais produtos? (S/N): ").strip().lower()
    # Enquanto a variável continuar for uma string vazia, ou continuar não estiver dentro da lista de opções disponíveis (s ou n):
    while not continuar or continuar[0] not in ("sn"):
        continuar = input("Opção inválida, por favor, digite novamente entre Sim (S), ou Não (N): ").strip().lower()
    print("-="*30, "\n")
    # Se o usuário digitar que não quer continuar cadastrando produtos:
    if continuar[0] == "n":
        break

# Mostra os valores finais para o usuário:
print(f"{" FIM DA COMPRA ":-^60}")
print(f"{produtos_cadastrados} produto(s) foi(foram) digitado(s).")
print(f"O VALOR TOTAL da compra foi R${valor_tot:.2f}.")
print(f"{mais_1000} produto(s) custa(m) MAIS DE R$1000.00.")
print(f"O produto mais CARO é {nome_caro}, com o valor de R${caro:.2f}. ", end="")
if caro > 1000:
    print(f"Inclusive, é um dos {mais_1000} produtos que custam mais de R$1000.00.")
print(f"O produto mais BARATO é {nome_barato}, com o valor de R${barato:.2f}. ")
