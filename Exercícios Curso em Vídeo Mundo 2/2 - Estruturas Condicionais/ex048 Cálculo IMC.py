print("-"*80)
print("                 CÁLCULO DE IMC (ÍNDICE DE MASSA CORPORAL)")
print("-"*80)
# IMC: Body Mass Index
# IMC: Índice de Massa Corporal

idade = int(input("Digite sua idade: "))
m = float(input("Digite a sua massa corporal (kg) (ex: 61): "))
a = float(input("Digite a sua altura em metros (ex: 1.80) (Caso for menor que 1 metro: ex 0.85): "))
print("-"*80)
imc = m / a**2
# If the age is less or equal to 1:
# Se a idade for menor ou igual a 1:
if idade <= 1:
    print("Você é muito novo para medir seu IMC! O mínimo é 2 anos.")
# If the age is between 2 and 5 years:
# Se a idade for entre 2 e 5 anos:
if idade >= 2 and idade <= 5:
    if imc < 14.5:
        print(f"IMC: {imc:.2f}. A criança está abaixo do peso, pois seu IMC é menor do que 14.5 pontos.")
    elif imc >= 14.5 and imc <= 17.0:
        print(f"IMC: {imc:.2f}. A criança está no seu peso ideal, pois seu IMC é entre 14.5 e 17.0 pontos.")
    elif imc >= 17.1 and imc <= 18.0:
        print(f"IMC: {imc:.2f}. A criança está acima do peso, pois seu IMC é entre 17.1 e 18.0 pontos.")
    elif imc > 18:
        print(f"IMC: {imc:.2f}. A criança está obesa, pois seu IMC ultrapassa 18 pontos.")
# If the age is between 6 and 9 years:
# Se a idade for entre 6 e 9 anos:
if idade >= 6 and idade <= 9:
    if imc < 14.0:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 14.0 pontos.")
    elif imc >= 14.0 and imc <= 19.0:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 14.0 e 19.0 pontos.")
    elif imc >= 19.1 and imc <= 21.0:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 17.1 e 18.0 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade, pois seu IMC ultrapassa os 18.0 pontos.")
# if the age is between 10 and 12 years:
# Se a idade for entre 10 e 12 anos:
if idade >= 10 and idade <= 12:
    if imc < 15.0:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 15.0 pontos.")
    elif imc >= 15.0 and imc <= 21.0:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 15.0 e 21.0 pontos.")
    elif imc >= 21.1 and imc <= 23.0:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 21.1 e 23.0 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade, pois seu IMC ultrapassa os 23.0 pontos.")
# If the age is between 13 and 15 years:
# Se a idade for entre 13 e 15 anos:
if idade >= 13 and idade <= 15:
    if imc < 16.0:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 16.0 pontos.")
    elif imc >= 15.0 and imc <= 23.0:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 16.0 e 23.0 pontos.")
    elif imc >= 23.1 and imc <= 25.0:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 23.1 e 25.0 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade, pois seu IMC ultrapassa os 25.0 pontos.")
# If the age is between 16 and 17 years:
# Se a idade for entre 16 e 17 anos:
if idade >= 16 and imc <= 17:
    if imc < 17.0:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 17.0 pontos.")
    elif imc >= 17.0 and imc <= 25.0:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 17.0 e 25.0 pontos.")
    elif imc >= 25.1 and imc <= 27.0:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 25.1 e 27.0 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade, pois seu IMC ultrapassa os 27.0 pontos.")
# If the age is between 18 and 64 years:
# Se a idade for entre 18 e 64 anos:
if idade >= 18 and idade <= 64:
    if imc < 18.5:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 17.0 pontos.")
    elif imc >= 18.5 and imc <= 24.9:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 17.0 e 25.0 pontos.")
    elif imc >= 25. and imc <= 29.9:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 25.1 e 27.0 pontos.")
    elif imc >= 30.0 and imc <= 34.9:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 1, pois seu IMC é entre 30.0 e 34.9 pontos.")
    elif imc >= 35.0 and imc <= 39.9:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 2, pois seu IMC é entre 35.0 e 39.9 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 3 (Obesidade mórbida), pois seu IMC ultrapassa os 40.0 pontos.")
# If the age is more than 65 years:
# Se a idade for mais que 65 anos:
if idade >= 65:
    if imc < 22.0:
        print(f"IMC: {imc:.2f}. Você está abaixo do peso, pois seu IMC é abaixo de 22.0 pontos.")
    elif imc >= 22.0 and imc <= 26.9:
        print(f"IMC: {imc:.2f}. Você está no seu peso ideal, pois seu IMC é entre 22.0 e 27.0 pontos.")
    elif imc >= 27.0 and imc <= 29.9:
        print(f"IMC: {imc:.2f}. Você está acima do peso, pois seu IMC é entre 27.0 e 29.9 pontos.")
    elif imc >= 30.0 and imc <= 34.9:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 1, pois seu IMC é entre 30.0 e 34.9 pontos.")
    elif imc >= 35.0 and imc <= 39.9:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 2, pois seu IMC é entre 35.0 e 39.9 pontos.")
    else:
        print(f"IMC: {imc:.2f}. Você está com obesidade grau 3, pois seu IMC ultrapassa os 40.0 pontos.")
