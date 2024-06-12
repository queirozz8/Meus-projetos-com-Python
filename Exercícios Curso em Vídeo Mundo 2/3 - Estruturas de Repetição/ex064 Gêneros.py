# [0] makes that regardless if the user types "male" rather than M, the software consider the same way, because he's taking just the first typed letter
# [0] faz com que independende se o usuário escrever "masculino" ao invés de M, ele considere da mesma forma, pois ele está pegando somente a primeira letra digitada
sexo = str(input("Digite seu gênero (M/F): ")).strip().upper()[0]
# While typed sex is not in the options available: (MmFf) 
# Enquanto o sexo digitado não estiver entre as opções disponíveis: (MmFf)
while sexo not in "MmFf":
    sexo = str(input("Opção inválida, por favor, digite seu sexo entre M ou F: "))
# When the user type M or F:
# Quando o usuário escrever M ou F:
print(f"Ok, sexo cadastrado como {sexo}, obrigado!")
