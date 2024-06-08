n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print(f"O {n1} (primeiro valor) é maior do que o {n2} (segundo valor).")
elif n2 > n1:
    print(f"O {n2} (segundo valor) é maior do que o {n1} (primeiro valor).")
else:
    print("Não há nenhum valor maior do que o outro, os dois são iguais.")
