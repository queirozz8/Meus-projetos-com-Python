# Todos os números de forma extensa armazenados em uma Tupla: 
numeros = ("zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove",
        "dez", "onze", "doze", "treze", "catorze",
        "quinze", "dezesseis", "dezessete", "dezoito", 
        "dezenove", "vinte")
while True:
    while True:
        num = int(input("Digite um número inteiro de 0 até 20 para eu escrever ele por extenso: "))
        # Se o número que o usuário digitar for maior ou igual à 0 mas menor ou igual à 20 (Se ele digitar um número entre o intervalo):
        if 0 <= num <= 20:
            break
        else:
            print("Número fora do intervalo. ", end="")
    # Fala o número por extenso:
    print(f"O número digitado foi {numeros[num]}.")
    continuar = ""
    # Enquanto a variável continuar estiver vazia ou a primeira letra digitada não estiver dentro das opções disponíveis (S ou N):
    while not continuar or continuar[0] not in "SN":
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break
print("Fim do Software, obrigado!")
