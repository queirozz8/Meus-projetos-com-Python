from datetime import date
# Total of peaple of legal age (21 years or more) (tot_Maior)
# Total of peaple below of legal age (below 21 years) (tot_Menor)
# Total de pessoas maiores de idade (21 anos ou mais) (tot_Maior)
# Total de pessoas menores de idade (menos de 21 anos) (tot_Menor)
tot_Maior = 0
tot_Menor = 0
ano_atual = date.today().year
for pessoa in range(1,8):
    nasc = int(input(f"Digite o ano que a {pessoa}° pessoa nasceu (ex: 1989): "))
    if nasc <= ano_atual - 21 and nasc > ano_atual - 90:
        tot_Maior += 1
    elif nasc > ano_atual - 21:
        tot_Menor += 1
    elif nasc < ano_atual - 90:
        print("Opção inválida, por favor, tente novamente com números de 1 até 90 anos.")
print(f"Pessoas maiores de idade: {tot_Maior}.")
print(f"Pessoas menores de idade: {tot_Menor}.")
