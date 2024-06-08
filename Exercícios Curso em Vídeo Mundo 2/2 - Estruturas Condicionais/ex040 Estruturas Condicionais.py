nome = str(input("Qual é o seu nome? "))
# If the name is Henrique:
# Se o nome for Henrique:
if nome == "Henrique":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("seu nome é bem popular no Brasil")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino!")
print(f"Tenha um bom dia, {nome}!")
