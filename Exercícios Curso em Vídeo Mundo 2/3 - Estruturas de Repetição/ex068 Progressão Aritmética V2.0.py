print("Gerador de PA")
print("-="*10)
termo = int(input("Digite o primeiro termo da sua PROGRESSÃO ARITMÉTICA: "))
razao = int(input("Digite a razão da sua PROGRESSÃO ARITMÉTICA: "))
cont = 1
print("A Progressão Aritmética é:")
while cont <= 10:
    # 'termo' it's going to be the numbers of the Arithmetic Progression, it's numbers
    # termo vai ser os números da Progressão Aritmética, vai ser os números dela
    print(f"{termo} → ", end="")
    # 'termo' (term) receives 'termo' + razao (difference), so if difference is 2 and the first term is 0, is "0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6, 6 + 2 = 8", and so on.
    # termo recebe termo + razao, então se a razão for 2 e o primeiro termo for 0, vai ser "0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6, 6 + 2 = 8" e assim por diante.
    termo += razao
    # Counter is who defines when the Software exits the loop
    # Contador é quem define quando o Software sai do loop
    cont += 1
print("FIM")
