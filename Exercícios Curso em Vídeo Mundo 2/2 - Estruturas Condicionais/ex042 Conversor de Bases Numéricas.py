numero = int(input("Digite um número inteiro para fazer a conversão: "))
conversao = int(input('''Selecione a base de conversão:
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL
Digite a opção: '''))
if conversao == 1:
    # "bin" transforms the number to binary
    # "bin" transforma o número em binário
    print(f"{numero} convertido para BINÁRIO é igual à {bin(numero)[2:]}")
elif conversao == 2:
    # "oct" transforms the number to octal
    # "oct" transforma o número em octal
    print(f"{numero} convertido para OCTAL é igual à {oct(numero)[2:]}")
elif conversao == 3:
    # "hex" transforms the number to hexadecimal
    # "hex" transforma o número em hexadecimal
    print(f"{numero} convertido para HEXADECIMAL é igual à {hex(numero)[2:]}")
else:
    print("Opção inválida. Tente novamente entre 1, 2 e 3.")
