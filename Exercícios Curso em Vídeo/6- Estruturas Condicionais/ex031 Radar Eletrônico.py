# Making the program header
# Fazendo o cabeçalho do programa
print("-="*15)
print("       RADAR ELETRÔNICO")
print("-="*15)
print("Limite de velocidade atual: 80km/h.")
velocidade = float(input("Qual é a velocidade atual do carro? "))

# If the speed was more than 80:
# Se a velocidade for maior que 80:
if velocidade > 80:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80km/h. Você utrapassou {velocidade - 80} do limite permitido.")
    multa = (velocidade-80) * 7 # It calculates how many the user is going to "pay" |  calcula o quanto o usuário deve "pagar"
    print(f"Você deve pagar uma multa de R$ {multa:.2f}.")
print("Tenha um bom dia! Dirija com segurança!")