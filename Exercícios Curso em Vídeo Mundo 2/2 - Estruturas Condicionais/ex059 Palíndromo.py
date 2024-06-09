# I prefer to do like this:
# Eu prefiro fazer assim:
# But we are practicing "for", so I'm going to use "for" for this software
# Mas nós estamos praticando o "for", então eu vou fazer esse software com o "for"
'''frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")'''
    
    
frase = str(input("Digite uma frase: ")).strip().upper()
# Each word is separated with the .split():
# Cada palavra é separada com o .split():
palavras = frase.split()
'''"junto" is the words together but separated by spaces, why does this variable exist? Because if the user types additional spaces, .strip() removes them all, and the "junto" variable adds spaces 
correct, a space to separate each word:'''
'''"junto" é as palavras juntas só que separadas por espaços, por que essa variável existe? Pois se o usuário digitar espaços adicionais, o .strip() remove todos, e a variável "junto" coloca espaços 
corretos, um espaço para separar cada palavra:'''
junto = "".join(palavras)
inverso = ""
# The inverse = the sentence joins starting from the beginning (:) and going to the end (:) but going backwards (-1):
# O inverso = a frase junta começando do início (:) e indo até o final (:) só que indo de trás para frente (-1):
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
