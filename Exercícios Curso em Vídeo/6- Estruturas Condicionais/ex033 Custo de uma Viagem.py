print("-="*20)
print("          CALCULADOR DE VIAGEM")
print("-="*20)
distancia = int(input("Digite a distância da sua viagem em km: (NÃO PRECISA DIGITAR 'KM', SÓ O NÚMERO): "))
print(f"Você está prestes a começar uma viagem de {distancia}km.")
print("Se a viagem for maior do que 200km, ela ganha um desconto, de R$ 0.50 por cada km, fica R$ 0.45 por cada km percorrido.")
# If the distance it's less or equal to 200:
# Se a distância for menor ou igual a 200:
if distancia <=200:
    preco = distancia * 0.50
else: # If it's more than 200, the price for every km is 0.45 |  Se for maior, o preço pra cada km fica 0.45
    preco = distancia * 0.45
print(f"O preço da sua passagem será de R$ {preco:.2f}")
