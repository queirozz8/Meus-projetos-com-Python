#EN: Requests the number
#BR: Solicita o número
num = int(input('Digite seu número de 0 até 9999: '))

#EN: It calculates units, tens, hundreds and thousands to show the category of each number
#BR: Faz a conta da unidade, dezena, centena e unidade de milhar, para mostrar a categoria de cada número
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#EN: Units:
#BR: Unidade:
print('Unidade: {}'.format(u))

#EN: Ten:
#BR: Dezena:
print('Dezena: {}'.format(d))

#EN: Hundred:
#BR: Centena:
print('Centena: {}'.format(c))

#EN: Unit of thousands:
#BR: Unidade de milhar:
print('Unidade de Milhar: {}'.format(m))
