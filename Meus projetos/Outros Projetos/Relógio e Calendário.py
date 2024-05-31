import datetime

# Header just for UX
# Cabeçalho só pelo UX
print("-" * 50)
print("{:^50}".format("CALENDÁRIO | RELÓGIO"))
print("-" * 50)
print()

def mostrar_data_hora():
    # It shows the date and time in a pretty way on the terminal.
    # Exibe a data e hora atual de forma bonita no terminal.
    agora = datetime.datetime.now()
    dia_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']  # Nomes completos dos dias da semana
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    print(f"📅   Hoje é {dia_semana[agora.weekday()]}, {agora.day} de {mes[agora.month - 1]} de {agora.year}")
    print(f"⏰   Agora são {agora.hour}:{agora.minute:02d}")
    print()
    print("Versão no calendário, o dia que está com dois '**' é o dia de hoje.")
    print()
    
    # Display the calendar.
    # Exibir o calendário.
    print("                           ", *{mes[agora.month - 1].upper()})
    print("{:^50}".format("   Dom     Seg       Ter      Qua     Qui      Sex      Sáb"))
    dia_atual = agora.day
    primeiro_dia_semana = (agora.replace(day=1)).weekday()  # Dia da semana do primeiro dia do mês
    ultimo_dia_mes = (agora.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)

    # Ajust the first day of the week to it initiate on Sunday.
    # Ajustar o primeiro dia da semana para iniciar no domingo.
    primeiro_dia_semana = (primeiro_dia_semana + 1) % 7

    # Fill in the days before the first day of the month.
    # Preencher os dias anteriores ao primeiro dia do mês.
    for i in range(primeiro_dia_semana):
        print("{:^9}".format(""), end="")

    # It shows every day of the month.
    # Exibir todos os dias do mês.
    for dia in range(1, ultimo_dia_mes.day + 1):
        if dia == dia_atual:
            print("{:^9}".format(f"**{dia}**"), end="")
        else:
            print("{:^9}".format(str(dia)), end="")
        if (dia + primeiro_dia_semana) % 7 == 0:
            print()

    print()
    
# At the end, it displays the calendar of the terminal.
# Por fim, mostra o calendário no terminal.
mostrar_data_hora()
