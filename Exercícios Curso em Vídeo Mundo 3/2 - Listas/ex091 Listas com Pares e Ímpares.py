print('-='*40)
print(f'{'LISTAS':^40}')
print('-='*40)

num = [[], []]
r = int(input('Quantos números deseja adicionar na sua lista? '))
for c in range(r):
    valor = int(input(f'Digite o {c+1}° número da sua lista: '))
    # Se o valor for par:
    if valor % 2 == 0:
        # Adicione o valor na primeira Sub-Lista; que eu defini como a Sub-Lista dos números pares:
        num[0].append(valor)
    else:
        # Adicione o valor na primeira Sub-Lista; que eu defini como a Sub-Lista dos números ímpares:
        num[1].append(valor)
print('-='*30)
# sorted ordena as Sub-Listas; map modifica todos os valores da lista para do tipo str (Eu criaria uma outra variável para fazer uma cópia dos elementos do num e transformaria 
# essa lista em strings, porém o exercício não pediu isso, então não tem porque deixar mais complicado atoa):
print(f'Os números PARES e de forma ORDENADA digitados foram: {', '.join(map(str, sorted(num[0]))) + '.'}')
print(f'Os números ÍMPARES e de forma ORDENADA digitados foram: {', '.join(map(str, sorted(num[1]))) + '.'}')