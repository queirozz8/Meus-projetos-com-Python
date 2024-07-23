import moeda

p = float(input('Digite o preço: R$'))
taxa_au = float(input('Quantos % de aumento? '))
taxa_di = float(input('Quantos % de desconto? '))
moeda.resumo(p, taxa_au, taxa_di)