# Lista de times do Brasileirão em ordem decrescente. Fonte: https://ge.globo.com/futebol/brasileirao-serie-a/
times = ("Flamengo", "Bahia", "Botafogo", "Palmeiras", "Cruzeiro", "Athletico-PR", "São Paulo",
         "Bragantino", "Internacional", "Atlético-MG", "Fortaleza", "Juventude", "Criciúma",
         "Cuiabá", "Vitória", "Vasco", "Atético-GO", "Corinthians", "Grêmio", "Fluminense")
print("CAMPEONATO BRASILEIRO DE FUTEBOL")
print(f"Tabela de times do Brasileirão, ordem decrescente:")
# Para cada time (20 times):
for cont_times in range(20):
    # Mostre o a colocação (número) do time atual, e mostre o nome do time (que está na tupla times) na posição do "time" (Contador do for loop):
    print(f"{cont_times+1}°: {times[cont_times]}", end="")
    # Se o contador do time for diferente de 19, mostre uma vírgula:
    if cont_times != 19:
        print(", ", end="")
    # Se o contador do time for igual à 19, mostre um ponto final (Pois esse é o último time que queremos mostrar):
    else:
        print(".")
print("-="*50, "\n")

# Pegue o índice do elemento "São Paulo" (+1, pois se não ele vai mostrar atrasado em 1):
print(f"São Paulo está em {times.index("São Paulo") + 1}° lugar.")
# Faça a mesma coisa com o Corinthians:
print(f"Corinthians está em {times.index("Corinthians") + 1}° lugar.")
print("-="*50, "\n")

print("Os primeiros colocados do Brasileirão são os times:")
# Para cada primeiro time dentro do range (5 times):
for cont_primeiros in range(5):
    # Mostre o número do contador atual (para representar a colocação do time) e mostre os times da tupla times na colocação do contador "primeiros":
    print(f"{cont_primeiros + 1}°: {times[cont_primeiros]}", end="")
    # Se o contador dos primeiros times for diferente de 4, mostre uma vírgula:
    if cont_primeiros != 4:
        print(", ", end="")
    # Se o contador dos primeiros times for igual à 4, mostre um ponto final (Pois esse é o último time que queremos mostrar):
    else:
        print(".")
print("-="*50, "\n")

print("Os últimos colocados do Brasileirão são os times:")
# Para cada último time (6 times):
for cont_ultimo in range(6):
    # Mostre o contador atual subtraído com 20 (Se o contador é 0: 0 - 20 = 20, 1 - 20 = 19, 2 - 20 = 18, e assim por diante. Isso representa a colocação dos últimos times)
    # E mostre a tupla dos times, só que na posição da lista ultimo subtraindo 19 (Ex: ultimo = 0. 0 - 19 = 19. 1 - 19 = 18, e assim por diante, isso faz com que ele acesse os 
    # # últimos elementos da tupla times):
    print(f"{20 - cont_ultimo}°: {times[19 - cont_ultimo]}", end="")
    # Se o contador dos últimos times for diferente de 5, mostre uma vírgula:
    if cont_ultimo != 5:
        print(", ",end="")
    # Se o contador dos últimos times for igual à 5, mostre um ponto final (Pois esse é o último time que queremos mostrar):
    else:
        print(".")
print("-="*50, "\n")

# Cria uma lista chamada times_org com os times ordenados em ordem alfabética:
times_org = sorted(times)
print(f"Times organizados em ordem alfabética:")
# Para cada time da lista organizada (20 times):
for cont_times_org in range(20):
    # Mostra o número do contador dos times ordenados (Para indicar a colocação do time), e mostra algum time da lista times_org, baseado no contador dos times ordenados:
    print(f"{cont_times_org + 1}°: {times_org[cont_times_org]}", end="")
    # Se o contador dos times ordenados for diferente de 19, mostre uma vírgula:
    if cont_times_org != 19:
        print(", ", end="")
    # Se o contador dos times ordenados foi igual à 19, mostre um ponto final (Pois esse é o último time que queremos mostrar):
    else:
        print(".")
print("-="*50)
print("FIM DO SOFTWARE, OBRIGADO!")
