print("         SOFTWARE TABUADA 3.0")
print("-="*20)
while True:
    numero = int(input("Deseja ver a tabuada de qual número (número inteiro)? (Digite 0 para parar): "))
    # Se o número digitado for 0:
    if numero == 0:
        print("-="*20)
        print("O número digitado foi 0. Software Tabuada 3.0 encerrado. Volte Sempre!")
        break
    print("-="*20)
    # Para cada número da tabuada (que é de 1 até 10):
    for tabuada in range(1, 11):
        print(f"{numero} x {tabuada} = {numero * tabuada}")
    print("-="*20)
