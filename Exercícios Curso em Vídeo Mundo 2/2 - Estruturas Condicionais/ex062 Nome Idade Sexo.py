soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ""
tot_mulher_20 = 0
print("Se você digitar o gênero da pessoa errado, o software vai pular ela. Não tem limite de idade, se colocar 0, o software vai contar ela, caso for mulher por exemplo, ele falará que essa mulher tem menos de 20 anos, obviamente.")
for pessoa in range(1, 5):
    print(f"----- {pessoa}° PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().lower()
    # soma_idade saves and sum the age of every peaple
    # soma_idade vai guardar e ir somando a idade de todas as pessoas:
    soma_idade += idade
    # If the person is the first of the list and is a man, who's the most old man and the name of the more old is him, because it doesn't have another person in the variable, so regardless of the values,
    # in the start, the variable receive the information:
    # Se a pessoa for a primeira da lista e for um homem, quem é o homem mais velho e o único nome do mais velho é ele, pois não tem outro na variável, então independente dos valores, no início, a variável 
    # recebe as informações:
    if pessoa == 1 and sexo == "m":
        maior_idade_homem = idade
        nome_velho = nome
    # If the current man is more old than the previous man:
    # Se o homem atual for mais velho que o homem de antes:
    if sexo == "m" and idade > maior_idade_homem:
        # The man is updated, he now is the oldest man, and he receives the "idade" (age) and the name that the user's gave in his turn:
        # O homem vai ser atualizado, ele passa a ser o homem mais velho, ele vai receber a idade e o nome que foram digitados na vez dele:
        nome_velho = nome
        maior_idade_homem = idade
    # If gender is not male or female (User typed wrong):
    # Se o sexo não for homem nem mulher (Usuário digitou errado):
    if sexo not in ["m", "f"]:
        print("Opção inválida, por favor, tente novamente com M (Masculino) ou F (Feminino).")
        continue
    # If a woman is less than 20 years old, the conter of women that have elss than 20 years old add 1 (tot_mulher_20)
    # Se uma mulher ter menos de 20 anos, o contador de mulheres que possuem menos de 20 anos acrescenta 1 (tot_mulher_20)
    if sexo in "Ff" and idade < 20:
        tot_mulher_20 += 1
# media_idade will calculate the medium of every ages that were saved and after this, added:
# media_idade vai calcular a média de todas as idades que foram armazenadas e depois somadas:
media_idade = soma_idade / 4
print(f"A média de idade do grupo é de {media_idade:.2f} anos.")
print(f"O homem mais velho se chama {nome_velho} e possui {maior_idade_homem} anos.")
print(f"Ao todo são {tot_mulher_20} mulher(es) com menos de 20 anos.")
