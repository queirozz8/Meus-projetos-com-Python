import moeda

p = float(input('Digite o preço: R$'))

# Mude para "False" ou remova o "True" caso não queira a formatação dos valores.
# moeda.moeda é: o 1° moeda significa o arquivo, a 'Biblioteca'. O 2° moeda significa a função, que é a função de formatação dos preços (nomeada de "moeda"):
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')

print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.')

print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}.')