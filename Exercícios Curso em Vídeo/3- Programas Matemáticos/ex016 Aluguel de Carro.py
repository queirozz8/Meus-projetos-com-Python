dias = int (input('Quantos dias o carro foi alugado? '))
km = float (input('Quantos Km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print ('O total a se pagar é R$ {:.2f}'.format (pago))
