print("-="*20)
print("     CALCULADOR DE VELOCIDADE MÉDIA")
print("-="*20)
distancia = float(input("Digite a distância de um ponto a outro (km): "))
tempo = float(input("Digite o tempo em que o veículo chegou de um ponto a outro (horas): "))
# Calculating the medium velocity. Formula: Distance of the trip divided by the time of the trip
# Calculando a velocidade média. Fórmula: Distância da viagem dividido pelo tempo da viagem
media = distancia / tempo
print("-"*70)
print(f"A velocidade média em que seu veículo estava era de {media}km/h.")
