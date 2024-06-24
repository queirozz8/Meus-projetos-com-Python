mais_18 = homens = mulheres_20 = 0
print("CADASTRADOR DE PESSOAS")
print("Este software conta quantas pessoas tem 18 ou mais anos de idade, quantos homens foram cadastrados e quantas mulheres com menos de 20 anos foram cadastradas.")
print("-"*157, "\n")
while True:
    print("-="*15)
    print("     CADASTRE UMA PESSOA")
    print("-="*15)
    idade = int(input("Digite a idade da pessoa: "))

    # Inicialmente, sexo começa sem nada:
    sexo = ""
    # Enquanto sexo for uma string vazia, ou a primeira letra da variável sexo não estiver na lista de sexos permitidos (m ou f):
    while not sexo or sexo[0] not in "mf":
        sexo = input("Digite o sexo da pessoa (M/F): ").strip().lower()

    # Se a idade for menor que 20 e o sexo for feminino:
    if idade < 20 and sexo == "f":
        mulheres_20 += 1

    # Se a idade for maior ou igual à 18:
    if idade >= 18: 
        mais_18 += 1

    # Se o sexo for masculino:
    if sexo == "m":
        homens += 1
    
    # Inicialmente, continuar começa sem nada:
    continuar = ""
    print("-"*20)
    # Enquanto continuar for uma string vazia, ou a primeira letra da variável continuar não estiver na lista de opções permitidas (s ou n):
    while not continuar or continuar not in "sn":
        continuar = input("Pessoa cadastrada. Deseja continuar? (S/N): ").strip().lower()
    # Se o usuário escolher que não quer cadastrar mais ninguém, o software sai do while loop:
    if continuar == "n":
        break

# Mostra os resultados das pessoas cadastradas ao usuário:
print(f"Ao todo, temos {mais_18} pessoa(s) com MAIS DE 18 ANOS.")
print(f"Ao todo, temos {homens} HOMEM(NS) cadastrado(s).")
print(f"E temos {mulheres_20} MULHER(ES) COM MENOS DE 20 ANOS.")
