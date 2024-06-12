from random import randint
print("        JOGUINHO DE ADIVINHAÇÃO")
print("-"*39)
# Previous configurations:
# Configurações prévias:
tentativas = 0
print("Vou pensar em um número inteiro entre 0 e 10, você precisa adivinhar ele!")
# Computer is going to randomize 10 numbers from 1 to 10, and it will choose 1 of them:
# Computador vai embaralhar 10 números de 1 até 10, e vai escolher 1 deles:
numero_computador = randint(1, 10)
palpite = int(input("Digite seu palpite: "))
# While 'palpite' (guess) it not the number that the computer thought:
# Enquanto o palpite não for o número que o computador pensou:
while palpite != numero_computador:
    # If 'palpite' (guess) is lower than 0 or higher than 10:
    # Se o palpite for menor do que 0 e maior do que 10:
    if palpite < 0 or palpite > 10:
        print("O número está entre 0 e 10, digite um número entre 0 e 10 para seu palpite, esse aqui não contou.")
    # If 'palpite' is lower than the computer's thought number:
    # Se o palpite for mais baixo que o número que o computador pensou:
    if palpite < numero_computador:
        palpite = int(input("Mais... o número é maior, tente de novo: "))
    # If 'palpite' is higher than the computer's thought number:
    # Se o palpite for maior do que o número que o computador pensou:
    elif palpite > numero_computador:
        palpite = int(input("Menos... o número é menor, tente de novo: "))
    # Add +1 for the attempts, if the user gets the number right, the Software exits from the 'while loop' and don't add +1 for the 'tentativas' (attempts)
    # Adiciona +1 às tentativas, se o usuário acertar o número, o Software sai do while e não adiciona +1 às tentativas:
    tentativas += 1
# When the user gets the number right, the Software shows him the computer's thought number and all the attempts the user tooked for him to get it right:
# Quando o usuário acerta o número, o Software mostra para ele o número que o computador pensou e todas as tentativas necessárias para o usuário acertar:
print(f"PARABÉNS, meu número era {numero_computador}. Você acertou meu número! Foram necessária(s) {tentativas} tentativa(s) para você adivinhar.")
