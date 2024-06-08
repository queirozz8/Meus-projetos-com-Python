from random import randint
from time import sleep
print("         PEDRA, PAPEL TESOURA (JOKENPÔ)")
print("-"*50)
escolha_Usuario = int(input('''PEDRA ganha da TESOURA, mas perde para o PAPEL, PAPEL ganha da pedra, mas perde para a TESOURA, TESOURA ganha do PAPEL, mas perde para a PEDRA.

[0] Para PEDRA
[1] Para PAPEL
[2] Para TESOURA
Digite a sua escolha: '''))
if escolha_Usuario > 3:
    print("Opção inválida. Escolha entre 1 (Pedra), 2 (Papel) ou 3 (Tesoura).")
itens = ("Pedra", "Papel", "Tesoura")
escolha_Computador = randint(0, 2)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")

print(f"O COMPUTADOR escolheu {itens[escolha_Computador]}")
print(f"O JOGADOR escolheu {itens[escolha_Usuario]}")

if escolha_Computador == 0: # Computador jogou PEDRA
    if escolha_Usuario == 0:
        print("EMPATE, pois uma pedra não ganha de outra pedra.")
    elif escolha_Usuario == 1:
        print("JOGADOR VENCEU, pois papel (Você) ganha da pedra (Computador).")
    elif escolha_Usuario == 2:
        print("COMPUTADOR VENCEU, pois pedra (Computador) ganha da tesoura (Você).")
elif escolha_Computador == 1: # Computador jogou PAPEL
    if escolha_Usuario == 0:
        print("COMPUTADOR VENCEU, pois papel (Computador) ganha da pedra (Você).")
    elif escolha_Usuario == 1:
        print("EMPATE, pois um papel não ganha de outro papel.")
    elif escolha_Usuario == 2:
        print("USUÁRIO VENCEU, pois tesoura (Você) ganha do papel (Computador).")
elif escolha_Computador == 2: # Computador jogou TESOURA
    if escolha_Usuario == 0:
        print("USUÁRIO VENCEU, pois pedra (você) ganha da tesoura (Computador).")
    elif escolha_Usuario == 1:
        print("COMPUTADOR VENCEU, pois tesoura (Computador) ganha do papel (Você).")
    elif escolha_Usuario == 2:
        print("EMPATE, pois uma tesoura não ganha de outra tesoura.")
