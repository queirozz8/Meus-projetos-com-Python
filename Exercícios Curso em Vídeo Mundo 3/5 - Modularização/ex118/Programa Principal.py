from utilidadesCeV import moeda, dado

p = dado.leia_dinheiro('Digite o preço: R$')
taxa_au = float(input('Quantos % de aumento? '))
taxa_di = float(input('Quantos % de desconto? '))
moeda.resumo(p, taxa_au, taxa_di)