print("Sequência de Fibonacci")
print("-="*10)
print("Sequência de fibonacci sempre começa com 0 e depois 1, o primeiro número soma com o segundo que dá o terceiro, ou seja, se o primeiro número é 1 e o segundo é 2, o terceiro número é 3 e assim em diante.")
# 'n' will represent how many numbers the user wants to see:
# 'n' vai representar quantos números o usuário quer ver:
n = int(input("Digite o número de termos que você quer ver da Sequência de Fibonacci: "))
# 't1' is the first term of the sequence, the sequence always starts at 0, so it starts with 0 too:
# 't1' é o primeiro termo da sequência, a Sequência sempre começa com 0, então ele começa inicialmente com 0 também:
t1 = 0
# 't2' is the second term of the sequence, after 0, the 2nd number is always 1:
# 't2' é o segundo termo da sequência, depois do 0, o segundo número é sempre 1:
t2 = 1
# Printing the 2 numbers:
# Mostrando os 2 números:
print(f"{t1} → {t2} → ", end="")
# 'cont' (Counter) is who will define how many times we are going to print t3, we already have printed t1 and t2, so the counter starts at 3:
# 'cont' (Contador) é quem vai definir quantas vezes iremos mostrar o t3, como já mostramos o t1 e t2, o contador começa com 3:
cont = 3
# While the counter doesn't get at the number that te user asked for:
# Enquanto o contador não chegar no número que o usuário pediu:
while cont <= n:
    # 't3' it's the number that we want to show, it's the number that succeeds t1 and t2, so t3 is the sum of t1 and t2:
    # 't3' é o número que queremos mostrar, é o número que sucede o t1 e t2, no caso, o t3 é a soma do t1 com t2:
    t3 = t1 + t2
    # Prints t3 on the Terminal
    # Escreve o t3 no Terminal
    print(f"{t3} → ", end="")
    # Substitui o t1 para a posição do t2, e o t2 para a posição do t3, assim, o t3 de novo é um número indefinido, que vai ser definido após esse loop voltar para o topo, fazendo a soma de t1 com t2 e 
    # descobrindo o t3, que vai ser exibido, enfim...
    t1 = t2
    t2 = t3
    # cont receives +1, for the loop don't start looping infinitely:
    # cont recebe +1, para o loop não ficar se repetindo infinitamente:
    cont += 1
# When the counter surpass the number that the user asked for (n), the Software exits from the While Loop and prints "FiM" (End) on the Terminal, after the arrow of the last number is typed:
# Quando o contador ultrapassar o número que o usuário pediu (n), o Software sai do While Loop e escreve "FIM" no Terminal, após a seta do último número ser escrita:
print("FIM.")
