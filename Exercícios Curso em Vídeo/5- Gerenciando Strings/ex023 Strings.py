# EN: Requests the user's full name.
# BR: Solicita o nome completo do usuário.
nome = str(input('Qual é o seu nome completo? '))
# EN: Separate the full name into parts.
# BR: Separa o nome completo em partes.
partes_do_nome = nome.split()
# EN: Separate the first name part.
# BR: Separa a parte do primeiro nome.
primeiro_nome = partes_do_nome[0]
# EN: Speaks the full name in capital letters, if the user has spoken in lower case letters.
# BR: Fala o nome completo em letras maiúsculas, caso o usuário tenha falado em letras minúsculas.
print('Seu nome completo é', nome.title())
# EN: Says greetings to the user and says the user's first name in capitalized form.
# BR: Diz saudações para o usuário e diz o primeiro nome do usuário de forma capitalizada.
print('Olá, {} '.format(primeiro_nome.title()))
