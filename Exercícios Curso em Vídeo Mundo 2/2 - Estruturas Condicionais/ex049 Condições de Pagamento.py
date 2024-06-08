print("-"*30)
print("           COMPRAS")
print("-"*30)
preco_Inicial = float(input("Qual é o preço pelas compras? R$"))
condicao_Pagamento = int(input('''Qual é a forma de pagamento?
[1] À vista dinheiro/Cheque (10% de desconto)
[2] À vista cartão (5% de desconto)
[3] Em até 2x no cartão (Valor original)
[4] 3x no cartão ou mais (20% de juros)
Digite o número da opção: '''))

# Se o usuário escolher pagar com dinheiro:
if condicao_Pagamento == 1:
    preco_Final = preco_Inicial * (1 - 10 / 100)
    print(f"Você pagará R${preco_Final:.2f} pelas compras com um desconto de 10% sobre o valor pois você está pagando com dinheiro/cheque à vista.")
# Se o usuário escolher pagar com cartão à vista:
elif condicao_Pagamento == 2:
    preco_Final = preco_Inicial * (1 - 5 / 100)
    print(f"Você pagará R${preco_Final:.2f} pelas compras com um desconto de 5% sem juros sobre o valor pois você está pagando com cartão à vista.")
# Se o usuário escolher parcelar em 2x:
elif condicao_Pagamento == 3:
    valor_Parcelas = preco_Inicial / 2
    print(f"Você pagará o valor original pois está pagando em 2x no cartão, então fica R${preco_Inicial:.2f}, você pagará R${valor_Parcelas} por 2 meses.")
# Se o usuário escolher parcelar entre 3x até 12x
elif condicao_Pagamento == 4:
    quantidade_Meses = int(input("Em quantos meses você vai pagar? Aceitamos até 12 meses: "))
    # Se o usuário escolher menos que 3 meses ou mais de 12 meses (Não é permitido):
    if quantidade_Meses > 12 or quantidade_Meses < 3:
        print("Nós não trabalhamos com prestações que tenham mais de 12 meses ou que tenham menos que 3 meses.")
    # Caso o usuário escolher entre 3 e 12 meses (Permitido):
    else:
        preco_Final = preco_Inicial * 1.20
        print(f"Você pagará R${preco_Final:.2f} pelas compras no fim, com juros de 20% sobre o valor pois você está pagando com cartão parcelado em 3 vezes ou mais.")
        valor_Parcelas = preco_Final / quantidade_Meses
        print(f"Você pagará {quantidade_Meses} parcelas de R${valor_Parcelas:.2f}.")
# Se o usuário não escolher entre as opções de pagamento disponíveis:
else:
    print("Opção inválida, por favor, digite uma opção válida entre 1, 2, 3 e 4.")
