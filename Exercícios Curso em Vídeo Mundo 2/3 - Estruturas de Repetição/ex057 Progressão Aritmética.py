print("  PROGRESSÃO ARITMÉTICA")
print("-"*25)
primeiro_Termo = int(input("Digite o primeiro termo da sua PROGRESSÃO ARITMÉTICA: "))
razao = int(input("Digite a razão da sua PROGRESSÃO ARITMÉTICA: "))
decimo = primeiro_Termo + (10-1) * razao
print("A progressão aritmética é:")
# For each number (10 numbers) of the arithmetic progression, show the numbers every so often, according to the ratio:
# Para cada número (10 números) da progressão aritmética, mostre os números de tanto em tanto, de acrodo com a razão:
for numero in range(primeiro_Termo, decimo + razao, razao):
    print(numero, end=" → ")
print("ACABOU")
