#EN: Requests the user's full name
#BR: Solicita o nome completo do usuário
nome = str(input('Qual é seu nome completo? ')).strip()

#EN: Look for the word silva somewhere in the full name, the program puts the full name in lowercase letters to avoid bugs as well.
#BR: Procura a palavra silva em algum lugar do nome completo, o programa coloca o nome completo em letras minúsculas pra evitar bugs também.
print ('Seu nome/sobrenome tem Silva? {}'.format('silva' in nome.lower()))
