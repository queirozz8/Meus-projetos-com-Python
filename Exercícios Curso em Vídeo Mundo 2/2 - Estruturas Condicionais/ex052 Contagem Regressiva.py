from time import sleep
print("CONTAGEM REGRESSIVA DOS FOGOS DE ARTIFÍCIO: ")
print("-"*50)
# "tempo" is going to be our counter of 1 to 10
# "tempo" vai ser nosso contador de 1 até 10
for tempo in range(10, -1, -1):
    print(f"{tempo}!")
    sleep(1) # Espera 1 segundo | Waits 1 second
print("OS FOGOS ESTOURARAM, KABOOM 🎆🧨")
