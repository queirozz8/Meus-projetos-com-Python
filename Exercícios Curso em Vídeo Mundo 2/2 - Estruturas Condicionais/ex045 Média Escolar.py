nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
# Calculate the average
# Faz o cálculo da média
media = (nota_1 + nota_2) / 2
# If the average is less than 5:
# Se a média for menor que 5:
if media < 5.0:
    print(f"A média das 2 notas do aluno foi {media:.1f}, ele foi REPROVADO.")
# If the average is between 5 and 7:
# Se a média for entre 5 e 7:
elif 7 > media >= 5:
    print(f"A média das 2 notas do aluno foi {media:.1f}, ele ficou de RECUPERAÇÃO.")
# If the average is more than 7:
# Se a média é maior do que 7:
elif media >= 7:
    print(f"A média das 2 notas do aluno foi {media:.1f}, ele foi APROVADO.")
